import logging

from .db_handler import JsonDb, SqliteDb


class DbAdapter:
    def __init__(self, db_type, table_name=None):
        try:
            self.db_handler = self.get_db_handler(db_type)
        except Exception as e:
            logging.critical(e)
            raise Exception("The application suffered a fatal error. Please restart.")

    def get_db_handler(self, db_type):
        # Sen: later change table_name thinguie. It'll be the job of the Db object.
        match db_type:
            case "sqlite":
                return SqliteDb()
            case "json":
                return JsonDb()
            case _:
                raise ValueError("Invalid database type.")

    def fetch_value(self, table_name, field, value):
        if field == "id":
            return self.db_handler.get_by_key(table_name, value)

    # Lucile: homemade ORM here?