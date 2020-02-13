from abc import ABC, abstractmethod
from copy import copy

from collections import deque

import pandas as pd
import logbook


from zipline.finance import trading
from zipline.data import loader as ld
from zipline.data import data_portal as dp
from zipline.protocol import BarData
from zipline.finance import asset_restrictions
from zipline.finance.order import ORDER_STATUS
from zipline.pipeline.data import USEquityPricing
from zipline.pipeline.loaders import USEquityPricingLoader
from zipline.utils import api_support

from pluto.coms.utils import conversions
from pluto.control.controllable import synchronization_states as ss
from pluto.finance.metrics import tracker
from pluto.sources import benchmark_source as bs
from pluto.data import bundler
from pluto.data.universes import universes

from protos import controllable_pb2

log = logbook.Logger('Controllable')


class _State(ABC):
    @abstractmethod
    def handle_data(self, algo, current_data, dt):
        raise NotImplementedError

    @abstractmethod
    def before_trading_starts(self, current_data, dt):
        raise NotImplementedError


class _Recovering(_State):
    def handle_data(self, algo, current_data, dt):
        # does nothing
        pass

    def before_trading_starts(self, algo, current_data):
        pass


class _Ready(_State):
    def handle_data(self, algo, current_data, dt):
        algo.event_manager.handle_data(algo, current_data, dt)

    def before_trading_starts(self, algo, current_dt):
        algo.before_trading_start(current_dt)


class Controllable(ABC):
    def __init__(self):
        self._metrics_tracker = None

        self._data_portal = None
        self._blotter = None
        self._asset_finder = None
        self._algo = None

        self._account = None
        self._current_data = None

        self._last_sync_time = None
        self._calculate_minute_capital_changes = None
        self._emission_rate = 'daily'
        self._data_frequency = 'daily'

        self._capital_change_deltas = {}
        self._capital_changes = {}

        # script namespace
        self._namespace = {}

        self._calendar = None
        self._universe = None
        self._calendars = None

        self._sessions = pd.Series()
        self._sessions_array = deque()

        self._session_id = None
        self._start_dt = None
        self._end_dt = None
        self._look_back = None
        self._current_dt = None
        self._params = None

        self._out_session = None
        self._active = None
        self._in_session = None
        self._bfs = None
        self._idle = None

        self._state = None

        self._ready = _Ready()
        self._recovering = recovering = _Recovering()
        self._run_state = recovering

    @property
    def out_session(self):
        return self._out_session

    @property
    def active(self):
        return self._active

    @property
    def in_session(self):
        return self._in_session

    @property
    def bfs(self):
        return self._bfs

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def calendars(self):
        return self._calendars

    @property
    def current_dt(self):
        return self._current_dt

    @property
    def run_state(self):
        return self._run_state

    @run_state.setter
    def run_state(self, value):
        self._run_state = value

    @property
    def recovering(self):
        return self._recovering

    @property
    def ready(self):
        return self._ready

    def initialize(self,
                   session_id,
                   start_dt,
                   end_dt,
                   universe,
                   strategy,
                   capital,
                   max_leverage,
                   data_frequency,
                   arena,
                   look_back):
        '''

        Parameters
        ----------
        start_dt: pandas.Timestamp
        end_dt: pandas.Timestamp
        universe: str
        strategy: bytes
        capital: float
        max_leverage: float
        data_frequency: str
        arena: str
        look_back: int

        '''

        self._last_sync_time = start_dt
        uni = universes.get_universe(universe)
        self._calendars = {cal:cal for cal in uni.calendars}

        self._out_session = ss.OutSession(self)
        self._active = ss.Active(self)
        self._in_session = ss.InSession(self)
        self._bfs = ss.Trading(self)
        self._idle = idle = ss.Idle(self)
        self._state = idle

        #load calendar by adding a day to avoid index errors
        calendar = uni.get_calendar(start_dt, end_dt + pd.Timedelta(days=1))
        self._session_id = session_id
        self._start_dt = start_dt
        # end_dt is the previous day
        self._end_dt = end_dt
        self._calendar = calendar
        self._universe = uni
        self._look_back = look_back
        self._data_frequency = data_frequency
        if data_frequency == 'minute':
            self._emission_rate = 'minute'

            def calculate_minute_capital_changes(dt, emission_rate):
                self._calculate_capital_changes(dt, emission_rate, is_interday=False)
        else:
            def calculate_minute_capital_changes(dt, emission_rate):
                return []

        self._calculate_minute_capital_changes = calculate_minute_capital_changes

        self._params = params = trading.SimulationParameters(
            start_dt,
            end_dt,
            calendar,
            capital,
            data_frequency=data_frequency,
            arena=arena)

        self._sessions = sessions = params.sessions
        self._sessions_array = deque(sessions)

        # we assume that the data has already been ingested => the controller must first
        # send data. An error is raised if there is no data
        loader = bundler.get_bundle_loader(uni.platform)
        bundle = loader(uni.bundle_name)
        self._asset_finder = asset_finder = bundle.asset_finder
        first_trading_day = bundle.equity_daily_bar_reader.first_trading_day

        #todo: equity_minute_bar_reader fix: should not instanciate the calendar
        #todo: equity_daily_reader should instanciate a calendar...
        self._data_portal = data_portal = dp.DataPortal(
            asset_finder=asset_finder,
            trading_calendar=calendar,
            first_trading_day=first_trading_day,
            # equity_minute_reader=bundle.equity_minute_bar_reader,
            equity_daily_reader=bundle.equity_daily_bar_reader,
            adjustment_reader=bundle.adjustment_reader)

        # load s&p 500 index as benchmark_asset.
        # todo: we can't load the benchmark data like this for now...
        # todo: we need a special file for benchmark data...
        # todo: '^GSPC' should be the benchmark...
        asset = asset_finder.lookup_symbol('AAPL', end_dt)
        # ld.load_market_data(calendar.day, sessions)

        # todo the benchmark creation should depend on the mode
        self._benchmark_source = benchmark_source = bs.SimulationBenchmarkSource(
            asset,
            calendar,
            sessions,
            self._data_portal,
            self._look_back,
            self._emission_rate)

        self._metrics_tracker = metrics_tracker = \
            tracker.MetricsTracker(
                benchmark_source,
                capital,
                data_frequency,
                start_dt,
                look_back)
        self._blotter = blotter = self._create_blotter()

        restrictions = asset_restrictions.NoRestrictions()

        self._current_data = self._create_bar_data(
            data_portal,
            calendar,
            restrictions,
            data_frequency)

        # todo: we need more pipeline loaders (fundamentals etc.)
        pipeline_loader = USEquityPricingLoader.without_fx(
            bundle.equity_daily_bar_reader,
            bundle.adjustment_reader,
        )

        def choose_loader(column):
            if column in USEquityPricing.columns:
                return pipeline_loader
            raise ValueError(
                "No PipelineLoader registered for column %s." % column
            )

        def noop(*args, **kwargs):
            pass

        code = compile(strategy, '', 'exec')
        exec(code, self._namespace)
        namespace = self._namespace

        # the algorithm object is just for exposing methods (api) that are needed by the user
        # (we don't run the algorithm through the algorithm object)

        # todo: the algo should call the data portal of the controllable, since it might be
        # re-assigned
        self._algo = algo = self._get_algorithm_class(
            params,
            data_portal,
            blotter,
            metrics_tracker,
            choose_loader,
            namespace.get('initialize', noop),
            namespace.get('handle_data', noop),
            namespace.get('before_trading_start', noop),
            namespace.get('analyze', noop))

        self._state = self._out_session
        self._run_state = self._ready
        # initialize the algo (called only once per lifetime)
        api_support.set_algo_instance(algo)
        algo.initialize(**{})  # todo: kwargs?
        algo.initialized = True

    @abstractmethod
    def _get_algorithm_class(self,
                             params,
                             data_portal,
                             blotter,
                             metrics_tracker,
                             get_pipeline_loader,
                             initialize,
                             before_trading_start,
                             handle_data,
                             analyze):
        '''
        Returns
        -------
        pluto.algorithm.TradingAlgorithm
        '''
        raise NotImplementedError(self._get_algorithm_class.__name__)

    def minute_end(self, dt):
        return self._get_minute_message(
            dt,
            self._algo,
            self._metrics_tracker,
            self._data_portal,
            self._calendar,
            self._sessions)

    def session_start(self, dt):

        end_dt = self._end_dt
        if dt > end_dt:
            # reload a new calendar
            self._start_dt = start_dt = dt - pd.Timedelta(days=self._look_back)
            self._end_dt = dt
            #todo: all the objects that depend on the calendar won't get this new value...
            #todo: add a day to dt
            #todo: reset all the instances that depend on the calendar:
            # -SimulationParameters <==== Reload entirely
            # -DataPortal <=== We need to reload this entirely

            self._calendar = self._universe.get_calendar(start_dt, dt)
            # updates the sessions (live)
            #FIXME: review this
            params = self._params
            sessions = self._sessions_array
            sessions.popleft()
            sessions.append(dt)
            params.start_session = sessions[0]
            params.end_session = dt
            self._sessions = pd.Series(sessions)

        self._sync_last_sale_prices(dt)
        self._calculate_capital_changes(dt, self._emission_rate, is_interday=False)

        algo = self._algo
        metrics_tracker = self._metrics_tracker
        data_portal = self._data_portal
        self._current_dt = dt

        algo.on_dt_changed(dt)
        metrics_tracker.handle_market_open(
            dt,
            data_portal,
            self._calendar,
            self._sessions)

        # handle any splits that impact any positions or any open orders.
        assets_we_care_about = (
                metrics_tracker.positions.keys() |
                algo.blotter.open_orders.keys()
        )

        if assets_we_care_about:
            splits = data_portal.get_splits(assets_we_care_about, dt)
            if splits:
                algo.blotter.process_splits(splits)
                metrics_tracker.handle_splits(splits)

    def before_trading_starts(self, dt):
        algo = self._algo
        self._current_dt = dt
        algo.on_dt_changed(dt)

        api_support.set_algo_instance(algo)
        self._run_state.before_trading_starts(algo, self._current_data)

    def bar(self, dt):
        self._sync_last_sale_prices(dt)
        self._current_dt = dt

        metrics_tracker = self._metrics_tracker

        algo = self._algo
        algo.on_dt_changed(dt)
        blotter = self._blotter

        calendar = self._calendar
        sessions = self._sessions

        capital_changes = self._calculate_minute_capital_changes(dt, self._emission_rate)

        # todo: assets must be restricted to the provided exchanges
        # self._restrictions.set_exchanges(exchanges)
        current_data = self._current_data

        new_transactions, new_commissions, closed_orders = blotter.get_transactions(current_data)

        blotter.prune_orders(closed_orders)

        for transaction in new_transactions:
            metrics_tracker.process_transaction(transaction)

            order = blotter.orders[transaction.order_id]
            metrics_tracker.process_order(order)

        for commission in new_commissions:
            metrics_tracker.process_commission(commission)

        # handle_data is not called while in recovery
        self._run_state.handle_data(algo, current_data, dt)

        # grab any new orders from the blotter, then clear the list.
        # this includes cancelled orders.
        new_orders = blotter.new_orders
        blotter.new_orders = []

        # if we have any new orders, record them so that we know
        # in what perf period they were placed.
        for new_order in new_orders:
            metrics_tracker.process_order(new_order)

        # todo: non-blocking!
        # todo: PROBLEM: we might have some conflicts in state, since we could have
        # multiple controllables with the same session_id running in different
        # modes...

        return capital_changes

    def session_end(self, dt):
        metrics_tracker = self._metrics_tracker

        positions = metrics_tracker.positions
        position_assets = self._asset_finder.retrieve_all(positions)
        blotter = self._blotter
        data_portal = self._data_portal
        calendar = self._calendar
        algo = self._algo

        self._cleanup_expired_assets(
            dt,
            data_portal,
            blotter,
            metrics_tracker,
            position_assets)

        algo.validate_account_controls()

        return self._get_daily_message(
            dt,
            algo,
            metrics_tracker,
            data_portal,
            calendar,
            self._sessions
        )

    def get_state(self, dt):
        metrics_tracker = self._metrics_tracker
        return controllable_pb2.ControllableState(
            session_id=self._session_id,
            session_state=self._state.name,
            capital=metrics_tracker.portfolio.cash,
            max_leverage=metrics_tracker.account.leverage,
            universe=self._universe.name,
            look_back=self._look_back,
            data_frequency=self._data_frequency,
            start=conversions.to_proto_timestamp(self._start_dt),
            end=conversions.to_proto_timestamp(self._end_dt),
            checkpoint=conversions.to_proto_timestamp(dt),
            metrics_tracker_state=metrics_tracker.get_state(dt)
        ).SerializeToString()

    def restore_state(self, state, strategy):
        self.initialize(
            state.session_id,
            conversions.to_datetime(state.start_dt),
            conversions.to_datetime(state.end_dt),
            state.universe,
            strategy,
            state.capital,
            state.max_leverage,
            state.data_frequency,
            state.mode,
            state.look_back)

        self._state = ss.get_state(state.session_state, self)
        self._current_dt = conversions.to_datetime(state.checkpoint)

    def stop(self, dt):
        # todo: liquidate all positions
        pass

    def update_blotter(self, broker_data):
        self._update_blotter(self._blotter, broker_data)

    @abstractmethod
    def _update_blotter(self, blotter, broker_data):
        raise NotImplementedError

    def update_account(self, main_account):
        self._update_account(self._blotter, main_account)

    @abstractmethod
    def _update_account(self, blotter, main_account):
        raise NotImplementedError

    def update_capital(self, dt, capital):
        self._capital_changes = {dt: {'type': 'target', 'value': capital}}

    @abstractmethod
    def _create_blotter(self, cancel_policy=None):
        raise NotImplementedError(self._create_blotter.__name__)

    def _get_daily_message(self, dt, algo, metrics_tracker, data_portal, trading_calendar, sessions):
        '''

        Parameters
        ----------
        dt
        algo: pluto.algorithm.TradingAlgorithm
        metrics_tracker: pluto.finance.metrics.tracker.MetricsTracker
        data_portal: zipline.data.data_portal.DataPortal
        trading_calendar: trading_calendars.TradingCalendar

        Returns
        -------

        '''
        """
        Get a perf message for the given datetime.
        """
        perf_message = metrics_tracker.handle_market_close(
            dt,
            data_portal,
            trading_calendar,
            sessions
        )
        perf_message['daily_perf']['recorded_vars'] = algo.recorded_vars
        return perf_message

    def _get_minute_message(self, dt, algo, metrics_tracker, data_portal, trading_calendar, sessions):
        '''

        Parameters
        ----------
        dt
        algo
        metrics_tracker: pluto.finance.metrics.tracker.MetricsTracker
        data_portal
        trading_calendar: trading_calendars.TradingCalendar

        Returns
        -------

        '''
        """
        Get a perf message for the given datetime.
        """
        rvars = algo.recorded_vars

        minute_message = metrics_tracker.handle_minute_close(
            dt,
            data_portal,
            trading_calendar,
            sessions
        )

        minute_message['minute_perf']['recorded_vars'] = rvars
        return minute_message

    def get_current_dt(self):
        return self._current_dt

    def _create_bar_data(self, data_portal, calendar, restrictions, data_frequency):
        return BarData(
            data_portal=data_portal,
            simulation_dt_func=self.get_current_dt,
            data_frequency=data_frequency,
            trading_calendar=calendar,
            restrictions=restrictions
        )

    def _cleanup_expired_assets(self, dt, data_portal, blotter, metrics_tracker, position_assets):
        '''

        Parameters
        ----------
        dt
        data_portal
        blotter
        metrics_tracker: pluto.finance.metrics.tracker.MetricsTracker
        position_assets

        Returns
        -------

        '''
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
        assets_to_clear = \
            [asset for asset in position_assets if past_auto_close_date(asset)]

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

    def _sync_last_sale_prices(self, dt=None):
        """Sync the last sale prices on the metrics tracker to a given
        datetime.

        Parameters
        ----------
        dt : datetime
            The time to sync the prices to.

        Notes
        -----
        This call is cached by the datetime. Repeated calls in the same bar
        are cheap.
        """
        if dt != self._last_sync_time:
            self._metrics_tracker.sync_last_sale_prices(
                dt,
                self._data_portal,
            )
            self._last_sync_time = dt

    def _calculate_capital_changes(self, dt, emission_rate, is_interday,
                                   portfolio_value_adjustment=0.0):
        """
        If there is a capital change for a given dt, this means that the change
        occurs before `handle_data` on the given dt. In the case of the
        change being a target value, the change will be computed on the
        portfolio value according to prices at the given dt

        `portfolio_value_adjustment`, if specified, will be removed from the
        portfolio_value of the cumulative performance when calculating deltas
        from target capital changes.
        """
        try:
            capital_change = self._capital_changes[dt]
        except KeyError:
            return

        if capital_change['type'] == 'target':
            target = capital_change['value']
            capital_change_amount = (
                    target -
                    (
                            self._metrics_tracker.portfolio.portfolio_value -
                            portfolio_value_adjustment
                    )
            )

            log.info('Processing capital change to target %s at %s. Capital '
                     'change delta is %s' % (target, dt,
                                             capital_change_amount))
        elif capital_change['type'] == 'delta':
            target = None
            capital_change_amount = capital_change['value']
            log.info('Processing capital change of delta %s at %s'
                     % (capital_change_amount, dt))
        else:
            log.error("Capital change %s does not indicate a valid type "
                      "('target' or 'delta')" % capital_change)
            return

        self._capital_change_deltas.update({dt: capital_change_amount})
        self._metrics_tracker.capital_change(capital_change_amount)

        yield {
            'capital_change':
                {'date': dt,
                 'type': 'cash',
                 'target': target,
                 'delta': capital_change_amount}
        }