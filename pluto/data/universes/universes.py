import abc

import sqlalchemy as sa

from protos import calendar_pb2

from pluto.data.universes import writer
from pluto.data.universes import schemas
from pluto.trading_calendars import calendar_utils as cu

engine = writer.engine


class AssetFilter(object):
    def __init__(self, directory):
        self._directory = directory

    def get_sids(self, dt):
        # returns a list of int for the given dt
        raise NotImplementedError(self.get_sids.__name__())


class AbstractUniverse(abc.ABC):
    @property
    @abc.abstractmethod
    def calendars(self):
        raise NotImplementedError(self.calendars.__name__())

    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplementedError(self.name.__name__())

    @abc.abstractmethod
    def get_calendar(self, start, end):
        raise NotImplementedError(self.get_calendar.__name__())

    @property
    @abc.abstractmethod
    def exchanges(self):
        raise NotImplementedError(self.exchanges.__name__())

    @property
    @abc.abstractmethod
    def bundle_name(self):
        raise NotImplementedError(self.bundle_name.__name__())

    @property
    @abc.abstractmethod
    def asset_filter(self):
        raise NotImplementedError(self.asset_filter.__name__())

    @property
    @abc.abstractmethod
    def platform(self):
        raise NotImplementedError(self.platform.__name__())


class Universe(AbstractUniverse):
    def __init__(self, name, directory):
        self._name = name
        self._directory = directory
        self._exchanges = None
        self._asset_filter = None
        self._calendar_path = None

    @property
    def name(self):
        return self._name

    @property
    def exchanges(self):
        # query the exchanges associated with this universe
        exchanges = self._exchanges
        if not exchanges:
            with engine.begin() as conn:
                stm = schemas.universes
                self._exchanges = \
                    exchanges = [
                    row[0]
                    for row in conn.execute(
                        sa.select([stm.c.exchange])
                            .join(schemas.universe_exchanges)
                            .where(stm.c.universe == self._name))]
        return exchanges

    def get_calendar(self, start, end):
        '''

        Parameters
        ----------
        start
        end

        Returns
        -------
        trading_calendars.TradingCalendar
        '''
        with engine.begin() as conn:
            stm = schemas.calendars
            result = conn.execute(
                sa.select([stm.c.file_path])
                    .join(schemas.calendar_exchanges)
                    .join(schemas.exchanges)
                    .where(*(stm.c.exchange == exchange
                             for exchange in self._exchanges)))
            self._calendar_path = cal_path = result.fetchone()['file_path']

        with open(cal_path) as f:
            proto = calendar_pb2.Calendar()
            proto.ParseFromString(f.read())

        return cu.from_proto_calendar(proto, start, end)

    @property
    def bundle_name(self):
        bundle = self._bundle_name
        if not bundle:
            with engine.begin() as conn:
                stm = schemas.universes
                result = conn.execute(
                    sa.select([stm.c.bundle])
                        .where(self._name == stm.c.universe))
                self._bundle_name = bundle = result.fetchone()['bundle']
        return bundle

    @property
    def asset_filter(self):
        # returns an asset filter of this universe
        asset_filter = self._asset_filter
        if not asset_filter:
            return AssetFilter(self._directory)
        else:
            return asset_filter

    @property
    def platform(self):
        return 'pluto'


class TestUniverse(AbstractUniverse):
    # for testing purposes, it is not meant to be
    # used in production
    @property
    def name(self):
        return 'test'

    @property
    def exchanges(self):
        return ('AMEX', 'NASDAQ', 'NYSE')

    @property
    def calendars(self):
        return ('XNYS',)

    def get_calendar(self, start, end):
        return cu.get_calendar_in_range('XNYS', start, end)

    @property
    def asset_filter(self):
        return None

    @property
    def platform(self):
        return 'zipline'

    @property
    def bundle_name(self):
        return 'quandl'

    def load_bundle(self):
        pass


def get_universe(name):
    '''

    Parameters
    ----------
    name: str

    Returns
    -------
    AbstractUniverse
    '''
    if name == 'test':
        return TestUniverse()
    else:
        return Universe(name, writer.get_directory(name))