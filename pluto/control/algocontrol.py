from concurrent import futures

from contextlib2 import ExitStack
from copy import copy
from logbook import Logger, Processor

import pandas as pd

from zipline.finance.order import ORDER_STATUS
from zipline.protocol import BarData
from zipline.utils.api_support import ZiplineAPI

from zipline.data import data_portal as dp
from zipline.finance import metrics
from zipline.finance import trading
from zipline.pipeline import data
from zipline.pipeline import loaders

from zipline import algorithm

from pluto.sources import benchmark_source as bs

log = Logger("ZiplineLog")


# todo: MetricsTracker and Account...

class BaseRunMode(object):
    "Encapsulates a set of methods for handling events"
    def on_bar(self, dt, algo, bar_data, metrics_tracker, data_portal, calendar, bundler, broker):
        """

        Parameters
        ----------
        dt
        metrics_tracker
        calendar
        bundler
        broker

        Returns
        -------

        """
        # compute capital changes and update account
        return self._capital_changes_and_metrics_update(
            algo, metrics_tracker, dt, data_portal,
            calendar, bundler.data_frequency, broker)

    def on_session_start(self, dt, bundler, calendar, metrics_tracker):
        # re-load attributes

        # compute eventual capital changes and update account
        return self._capital_changes_and_metrics_update(
            self._algo, metrics_tracker, dt,
            self._data_portal, calendar, bundler.data_frequency
        )

    def on_session_end(self, dt, algo, data_portal, metrics_tracker, data_frequency):
        return self._get_daily_message(dt, algo, metrics_tracker, data_portal)

    def on_minute_end(self, dt, algo, data_portal, metrics_tracker):
        return self._get_minute_message(
            dt,
            algo,
            metrics_tracker,
            data_portal
        )

    def _get_daily_message(self, dt, algo, metrics_tracker, data_portal):
        """
        Get a perf message for the given datetime.
        """
        perf_message = metrics_tracker.handle_market_close(
            dt,
            data_portal,
        )
        perf_message['daily_perf']['recorded_vars'] = algo.recorded_vars
        return perf_message

    def _get_minute_message(self, dt, algo, metrics_tracker, data_portal):
        """
        Get a perf message for the given datetime.
        """
        rvars = algo.recorded_vars

        minute_message = metrics_tracker.handle_minute_close(
            dt,
            data_portal,
        )

        minute_message['minute_perf']['recorded_vars'] = rvars
        return minute_message

    def _cleanup_expired_assets(self, dt, blotter, position_assets, data_portal, metrics_tracker):
        """
        Clear out any assets that have expired before starting a new sim day.

        Performs two functions:

        1. Finds all assets for which we have open orders and clears any
           orders whose assets are on or after their auto_close_date.

        2. Finds all assets for which we have positions and generates
           close_position events for any assets that have reached their
           auto_close_date.
        """

        def past_auto_close_date(asset):
            acd = asset.auto_close_date
            return acd is not None and acd <= dt

        # Remove positions in any sids that have reached their auto_close date.
        assets_to_clear = [asset for asset in position_assets if past_auto_close_date(asset)]
        for asset in assets_to_clear:
            metrics_tracker.process_close_position(asset, dt, data_portal)

        # Remove open orders for any sids that have reached their auto close
        # date. These orders get processed immediately because otherwise they
        # would not be processed until the first bar of the next day.
        assets_to_cancel = [
            asset for asset in blotter.open_orders
            if past_auto_close_date(asset)
        ]
        for asset in assets_to_cancel:
            blotter.cancel_all_orders_for_asset(asset)

        # Make a copy here so that we are not modifying the list that is being
        # iterated over.
        for order in copy(blotter.new_orders):
            if order.status == ORDER_STATUS.CANCELLED:
                metrics_tracker.process_order(order)
                blotter.new_orders.remove(order)

    def _capital_changes_and_metrics_update(self, algo, metrics_tracker, dt, data_portal,
                                            trading_calendar, data_frequency, broker):
        cap_change = metrics_tracker.update(dt, data_portal, trading_calendar,
                                            data_frequency, self._capital_target, broker)

        self._capital_target = None
        self._run_dt = dt
        algo.on_dt_changed(dt)
        return cap_change


class AlgorithmController(object):
    """Controls variables lifetime"""

    def __init__(self, control_mode, strategy, benchmark_asset, restrictions, state_storage_path):
        """

        Parameters
        ----------
        strategy
        benchmark_asset
        restrictions : zipline.finance.asset_restrictions.Restrictions
        """

        self._stack = ExitStack()

        self._strategy = strategy

        self._algo = None

        self._data_portal = None

        self._run_dt = None

        # todo: need to validate the benchmark asset.
        self._benchmark_source = bs.BenchmarkSource(benchmark_asset)

        self._restrictions = restrictions

        self._current_data = None

        # Processor function for injecting the algo_dt into
        # user prints/logs.
        def inject_algo_dt(record):
            if 'algo_dt' not in record.extra:
                record.extra['algo_dt'] = self._get_run_dt

        self._processor = Processor(inject_algo_dt)

        self._last_sync_time = pd.NaT

        self._capital_target = None

        self._pool = futures.ProcessPoolExecutor()

        self._mode = control_mode

        self._ssp = state_storage_path

    def on_initialize(self, dt, metrics_tracker, bundler, calendar, emission_rate, capital, state_storage_path):
        # initialize all attributes
        self._load_attributes(dt, bundler.load(), calendar, emission_rate, initialize=True)
        # check if there is a previously stored state.
        try:
            with open(state_storage_path, "rb") as f:
                metrics_tracker.restore_state(f.read())
        except FileNotFoundError:
            metrics_tracker.handle_initialization(dt, calendar.session_open(dt), capital)

    def on_bar(self, dt, calendar, bundler, metrics_tracker, emission_rate):
        self._load_attributes(dt, bundler.load(), calendar, emission_rate)

        algo = self._algo
        self._run_dt = dt

        self._mode.on_bar(dt, algo, metrics_tracker)

        # make a checkpoint of the state of the tracker as a sub-process
        self._pool.submit(self._store_state, path=self._ssp, state=metrics_tracker.get_state(dt))

        algo.event_manager.handle_data(algo, self._current_data, dt)

    def on_session_start(self, dt, calendar, metrics_tracker):
        self._run_dt = dt
        metrics_tracker.handle_market_open(dt, self._data_portal, calendar)

    def on_session_end(self, dt, metrics_tracker, data_frequency):
        algo = self._algo
        dp = self._data_portal

        if data_frequency == 'minute':
            def execute_order_cancellation_policy(blotter, event):
                blotter.execute_cancel_policy(event)

        else:
            def execute_order_cancellation_policy():
                pass

        execute_order_cancellation_policy()
        algo.validate_account_controls()

        return self._mode.on_session_end(dt, algo, metrics_tracker)
        # handle the session end (create and store bundle for future load)
        # bundler.on_session_end(dt)

    def on_before_trading_start(self, dt):
        algo = self._algo
        self._run_dt = dt
        algo.on_dt_changed(dt)
        algo.before_trading_start(self._current_data)

    def on_minute_end(self, dt, metrics_tracker):
        self._mode.on_minute_end(dt, self._algo, self._data_portal, metrics_tracker)

    def on_stop(self, dt, metrics_tracker):
        # save the state of the tracker (and account) before shutting down...
        metrics_tracker.handle_stop(dt)
        with open(self._ssp, "wb") as f:
            f.write(metrics_tracker.get_state(dt))

    def on_liquidate(self, dt, metrics_tracker):
        metrics_tracker.handle_liquidation(dt)

    def _get_run_dt(self):
        return self._run_dt

    def set_broker(self, broker):
        self._broker = broker

    def set_capital_target(self, value):
        self._capital_target = value

    def _store_state(self, path, state):
        with open(path, "wb") as f:
            f.write(state)

    def _create_bar_data(self, data_portal, get_simulation_dt, data_frequency, calendar, restrictions):
        return BarData(
            data_portal=data_portal,
            simulation_dt_func=get_simulation_dt,
            data_frequency=data_frequency,
            trading_calendar=calendar,
            restrictions=restrictions)


    def _load_data_portal(self, calendar, asset_finder, first_trading_day,
                          equity_minute_bar_reader, equity_daily_bar_reader,
                          adjustment_reader):
        return dp.DataPortal(
            asset_finder,
            trading_calendar=calendar,
            first_trading_day=first_trading_day,
            equity_minute_reader=equity_minute_bar_reader,
            equity_daily_reader=equity_daily_bar_reader,
            adjustment_reader=adjustment_reader
        )

    # todo: we don't need a metrics_set here...
    def _create_algorithm(self, start_session, end_session, capital_base, namespace, data_portal,
                          get_pipeline_loader, calendar, emission_rate, blotter, data_frequency='daily',
                          metrics_set='default', benchmark_returns=None):
        return algorithm.TradingAlgorithm(
            namespace={},
            data_portal=data_portal,
            get_pipeline_loader=get_pipeline_loader,
            trading_calendar=calendar,
            sim_params=trading.SimulationParameters(
                start_session=start_session,
                end_session=end_session,
                trading_calendar=calendar,
                capital_base=capital_base,
                data_frequency=data_frequency,
                emission_rate=emission_rate
            ),
            metrics_set=metrics.load(metrics_set),
            blotter=blotter,
            benchmark_returns=benchmark_returns,
            **{
                'initialize': self._strategy.initialize,
                'handle_data': self._strategy.handle_data,
                'before_trading_start': self._strategy.before_trading_start,
                'analyze': self._strategy.analyze
            }
        )

    def _load_attributes(self, dt, bundle, calendar, emission_rate, data_frequency='daily', initialize=False):
        equity_minute_reader = bundle.equity_minute_bar_reader
        self._asset_finder = asset_finder = bundle.asset_finder
        self._data_portal = portal = self._load_data_portal(
            calendar, asset_finder, equity_minute_reader.first_trading_day,
            equity_minute_reader, bundle.equity_daily_bar_reader, bundle.adjustment_reader
        )

        self._current_data = self._create_bar_data(
            portal,
            self._get_run_dt,
            data_frequency,
            calendar,
            self._restrictions
        )

        pipeline_loader = loaders.USEquityPricingLoader(
            # use the current bundle's readers
            bundle.equity_daily_bar_reader,
            bundle.adjustment_reader
        )

        def choose_loader(column):
            if column in data.USEquityPricing.columns:
                return pipeline_loader
            raise ValueError(
                "No PipelineLoader registered for column %s." % column
            )

        self._algo = algo = self._create_algorithm(
            start_session=dt,
            calendar=calendar,
            data_portal=self._data_portal,
            get_pipeline_loader=choose_loader,
            emission_rate=emission_rate)  # todo

        # initialize algorithm object
        algo.on_dt_changed(dt)
        if initialize:
            algo.initialize()

    # todo: handle_start_of_simulation (for metrics_tracker etc.)

    def __enter__(self):
        stack = self._stack
        stack.enter_context(self._processor)
        stack.enter_context(ZiplineAPI(self._algo))

        def on_exit():
            # Remove references to algo, data portal, et al to break cycles
            # and ensure deterministic cleanup of these objects when the
            # simulation finishes.
            self._algo = None
            self.benchmark_source = self.current_data = self.data_portal = None

        stack.callback(on_exit)

    def __exit__(self, *exc_details):
        self._stack.close()
