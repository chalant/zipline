from collections import Iterable

from pluto.data.universes import schemas
from pluto.interface.utils import paths, db_utils

_ROOT  = paths.get_dir('data')
_DIRECTORY = paths.get_dir('universes', _ROOT)
_FILE = paths.get_file_path('metadata', _DIRECTORY)

engine = db_utils.create_engine(_FILE)
metadata = schemas.metadata
metadata.create_all(engine)

#todo: write asset into a bcolz table where each column is a all the assets at a given
# timestamp.
# we should be able to append new data to the table etc.
# we should be able to store metadata about the universe, like exchanges etc.

class UniverseWriter(object):
    def __init__(self, directory, universe_name):
        self._directory = directory

    def write(self, exchanges, dt_sids_mappings):
        #todo: add the universe_name to the universe_calendars table with the corresponding
        # exchanges
        '''

        Parameters
        ----------
        exchanges: list[str]
                list of exchanges associated with the universe
        dt_sids_mappings: Iterable[datetime.datetime, Iterable[int]]
        '''
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def get_directory(universe_name):
    return paths.get_dir(universe_name, _DIRECTORY)

def get_writer(universe_name):
    #todo: insert the universe_name in the metadata

    #todo: there are two steps when writing data: there is "prepolulation"
    # where we write all the data (+ historical)
    # then there is update, where we append data each clock event, such as minute_end
    # or session_end
    return UniverseWriter(get_directory(universe_name), universe_name)