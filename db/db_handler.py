import logging, sqlite3

from pathlib import Path

from .serialisers import DomainSerialiser

def get_db_path():
    return Path(__file__).parents[0] / 'sqlite.db'

class BaseDbHandler:
    @staticmethod
    def db_access_wrapper(func):
        def wrapper_func(self, *args, **kwargs):
            try:
                db_path = get_db_path()
                with sqlite3.connect(db_path) as conn:
                    return func(self, conn, *args, **kwargs)
            except Exception as e:
                error_msg = f"Error while trying to connect to db: {e}"
                logging.critical(error_msg)
                raise ConnectionError(error_msg)

        return wrapper_func

    @db_access_wrapper
    def check_tables_integrity(self, conn) -> None:
        # TODO: later on, check that table = Serialiser template
        cursor = conn.cursor()
        list_of_serialisers = [DomainSerialiser,]
        list_of_missing_tables = []

        for serialiser in list_of_serialisers:
            table_exists = self.table_exists(cursor, serialiser.table_name)
            if not table_exists:
                list_of_missing_tables.append(serialiser.table_name)
        
        if len(list_of_missing_tables) > 0:
            logging.critical(f"Missing tables: {list_of_missing_tables}")
            raise ConnectionRefusedError("Missing tables: please see logs.")

    def table_exists(self, cursor, table_name):
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        return cursor.fetchone() is not None
        
    # TODO: fit either none, one or many criterias.
    def get(self, table_name):
        pass

    def update(self, table_name):
        pass

    def insert(self, table_name):
        pass

    def delete(self, table_name):
        pass


class SqlDbHandler(BaseDbHandler):
    pass