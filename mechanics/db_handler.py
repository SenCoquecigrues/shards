import logging

from db.json_adapter import JsonSaveAdapter

class DbHandler:
    def __init__(self, db_type, table_name=None):
        try:
            self.db_handler = self.get_db_handler(db_type, table_name)
        except Exception as e:
            logging.critical(e)
            raise Exception("The application suffered a fatal error. Please restart.")

    def get_db_handler(self, db_type, table_name=None):
        match db_type:
            case "sqlite":
                pass
            case "json":
                return JsonSaveAdapter(table_name)
            case _:
                raise ValueError("Invalid database type.")

    def fetch_value(self, field, value):
        if field == "id":
            return self.db_handler.get_by_id(value)
