import abc
from collections import deque

import pandas as pd
import numpy as np

from zipline.errors import (
    InvalidBenchmarkAsset,
    BenchmarkAssetNotAvailableTooEarly,
    BenchmarkAssetNotAvailableTooLate
)

from zipline.finance._finance_ext import minute_annual_volatility


class BenchmarkSource(abc.ABC):
    def __init__(self,
                 benchmark_asset,
                 trading_calendar,
                 sessions,
                 data_portal,
                 look_back,
                 emission_rate="daily"):
        '''

        Parameters
        ----------
        benchmark_asset
        trading_calendar: trading_calendars.TradingCalendar
        sessions
        data_portal: zipline.data.data_portal.DataPortal
        emission_rate
        '''
        self._benchmark_asset = benchmark_asset
        self._emission_rate = emission_rate

        self._start_dt = start = sessions[0]
        self._end_dt = end = sessions[-1]
        self._open_dt = trading_calendar.session_open(start)
        self._minute_end_dt = trading_calendar.session_close(end)

        self._look_back = look_back

        self._daily_returns = None
        self._cumulative_returns = None
        self._annual_volatility = None

        self._minute_annual_volatility = None
        self._minute_cumulative_returns = None

        self._session_idx = -1
        self._daily_index = -1
        self._minute_index = -1
        self._minute_recomputed = False
        self._day_recomputed = False

        self._daily_returns_array = deque()
        self._minute_returns_array = deque()

        if len(sessions) == 0:
            self._precalculated_series = pd.Series()
        else:
            self._validate_benchmark(benchmark_asset, sessions, data_portal)
            # in live, we get the previous session, and in simulation we get the current session.
            self._precalculated_series, self._daily_returns = \
                self._calculate_benchmark_series(
                    benchmark_asset,
                    sessions,
                    data_portal,
                    trading_calendar,
                    emission_rate,
                    end + pd.Timedelta('1 Day'))
            returns = self._daily_returns
            self._cumulative_returns = np.cumprod(1 + returns.values) - 1
            self._annual_volatility = (
                    returns.expanding(2).std(ddof=1) * np.sqrt(252)).values

            if self._emission_rate == 'minute':
                p_returns = self._precalculated_series
                self._minute_cumulative_returns = np.cumprod(1 + p_returns.values) - 1
                self._minute_annual_volatility = (
                        returns.expanding(2).std(ddof=1) * np.sqrt(252)).values

    def on_session_start(self, sessions):
        self._start_dt = sessions[0]
        self._session_idx += 1

    def on_session_end(self, data_portal, trading_calendar, sessions):
        end = sessions[-1]
        if self._emission_rate == 'daily':
            if self._recompute_hook():
                # only compute if the emission_rate is daily
                self._precalculated_series, self._daily_returns = \
                    self._calculate_benchmark_series(
                        self._benchmark_asset,
                        sessions,
                        data_portal,
                        trading_calendar,
                        'daily',
                        end
                    )
                returns = self._precalculated_series
                self._cumulative_returns = np.cumprod(1 + returns.values) - 1
                self._annual_volatility = (returns.expanding(2).std(ddof=1) * np.sqrt(252)).values
                self._daily_index = -1
                self._day_recomputed = True

        if not self._day_recomputed:
            self._daily_index += 1

        returns = self._daily_returns_array
        if self._session_idx == self._look_back:
            returns.popleft()
            self._session_idx = 0
        returns.append(self._daily_returns[self._daily_index])

        start = sessions[0]
        self._open_dt = trading_calendar.session_open(start)
        self._minute_end_dt = trading_calendar.session_close(end)
        self._end_dt = end

    def on_minute_end(self, dt, data_portal, trading_calendar, sessions):
        if self._emission_rate == 'minute':
            if self._recompute_hook():
                self._precalculated_series, self._daily_returns = \
                    self._calculate_benchmark_series(
                        self._benchmark_asset,
                        sessions,
                        data_portal,
                        trading_calendar,
                        'minute',
                        dt)
                period_returns = self._precalculated_series.values
                self._minute_cumulative_returns = np.cumprod(1 + period_returns) - 1
                self._mminute_annual_volatility = minute_annual_volatility(
                    period_returns.index.normalize().view('int64'),
                    period_returns.values,
                    self._daily_returns.values)
                self._minute_index = -1
                self._minute_recomputed = True

            if not self._minute_recomputed:
                self._minute_index += 1
            self._minute_end_dt = dt

    @abc.abstractmethod
    def _recompute_hook(self):
        # check whether we should recompute the series.
        raise NotImplementedError

    def daily_returns(self):
        return np.array(self._daily_returns_array)

    @property
    def cumulative_returns(self):
        return self._cumulative_returns[self._daily_index]

    @property
    def annual_volatility(self):
        return self._annual_volatility[self._daily_index]

    @property
    def minute_cumulative_returns(self):
        return self._minute_cumulative_returns[self._minute_index]

    @property
    def minute_annual_volatility(self):
        return self._minute_annual_volatility[self._minute_index]

    def get_range(self):
        series = self._precalculated_series
        if series:
            return series.loc[self._open_dt:self._minute_end_dt]
        return

    def _calculate_benchmark_series(self, asset, sessions, data_portal, trading_calendar, emission_rate, end_dt):
        # FIXME: we are reloading all series at each call. We only need the previous and most recent price
        # => load a window of length 2, calculate percentage change, append it to returns array
        # when we pre-calculate, we load a data window ending at the most recent close datetime, then
        # append newly computed data to it...
        # formula: (v2 - v1)/v1

        if emission_rate == "minute":
            # calculate returns until most recent minute end
            # FIXME: the last minute will be either below or equal to end_dt...
            # simulation expects minutes above end_dt as-well... add one day in sim?
            minutes = trading_calendar.minutes_in_range(sessions[0], end_dt)
            benchmark_series = data_portal.get_history_window(
                [asset],
                minutes[-1],
                bar_count=len(minutes),
                frequency="1m",
                field="price",
                data_frequency=emission_rate,
                ffill=True
            )[asset]

            return (
                benchmark_series.pct_change(),
                self.downsample_minute_return_series(trading_calendar, benchmark_series))

        start_date = asset.start_date

        first_trading_day = sessions[0]
        last_trading_day = sessions[-1]

        if start_date < first_trading_day:
            # get the window of close prices for benchmark_asset from the
            # last trading day of the simulation, going up to one day
            # before the simulation start day (so that we can get the %
            # change on day 1)
            benchmark_series = data_portal.get_history_window(
                [asset],
                last_trading_day,
                bar_count=len(sessions),
                frequency="1d",
                field="price",
                data_frequency=emission_rate,
                ffill=True
            )[asset]

            # benchmark_series.to_csv('benchmark_series')
            returns = benchmark_series.pct_change()
            returns[0] = 0
            return returns, returns
        elif start_date == first_trading_day:
            # Attempt to handle case where stock data starts on first
            # day, in this case use the open to close return.
            benchmark_series = data_portal.get_history_window(
                [asset],
                last_trading_day,
                bar_count=len(sessions),
                frequency="1d",
                field="price",
                data_frequency=emission_rate,
                ffill=True
            )[asset]

            # get a minute history window of the first day
            first_open = data_portal.get_spot_value(
                asset,
                'open',
                first_trading_day,
                'daily',
            )
            first_close = data_portal.get_spot_value(
                asset,
                'close',
                first_trading_day,
                'daily',
            )

            first_day_return = (first_close - first_open) / first_open

            returns = benchmark_series.pct_change()
            returns[0] = first_day_return
            return returns, returns
        else:
            raise ValueError(
                'cannot set benchmark to asset that does not exist during'
                ' the simulation period (asset start date=%r)' % start_date
            )

    def _validate_benchmark(self, benchmark_asset, sessions, data_portal):
        # check if this security has a stock dividend.  if so, raise an
        # error suggesting that the user pick a different asset to use
        # as benchmark.
        stock_dividends = \
            data_portal.get_stock_dividends(benchmark_asset,
                                            sessions)

        if len(stock_dividends) > 0:
            raise InvalidBenchmarkAsset(
                sid=str(benchmark_asset),
                dt=stock_dividends[0]["ex_date"]
            )

        if benchmark_asset.start_date > sessions[0]:
            # the asset started trading after the first simulation day
            raise BenchmarkAssetNotAvailableTooEarly(
                sid=str(benchmark_asset),
                dt=sessions[0],
                start_dt=benchmark_asset.start_date
            )

        if benchmark_asset.end_date < sessions[-1]:
            # the asset stopped trading before the last simulation day
            raise BenchmarkAssetNotAvailableTooLate(
                sid=str(benchmark_asset),
                dt=sessions[-1],
                end_dt=benchmark_asset.end_date
            )

    @classmethod
    def downsample_minute_return_series(cls, trading_calendar, minutely_returns):
        sessions = trading_calendar.minute_index_to_session_labels(
            minutely_returns.index,
        )
        closes = trading_calendar.session_closes_in_range(
            sessions[0],
            sessions[-1],
        )
        daily_returns = minutely_returns[closes].pct_change()
        daily_returns.index = closes.index
        return daily_returns.iloc[1:]

    def get_value(self, dt):
        return self._precalculated_series.loc[dt]


class SimulationBenchmarkSource(BenchmarkSource):
    def _recompute_hook(self):
        return False


class LiveBenchmarkSource(BenchmarkSource):
    def _recompute_hook(self):
        return True