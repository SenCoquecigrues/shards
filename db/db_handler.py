import json
import sqlite3

from pathlib import Path


class DBHandler:
    # TODO: fit either none, one or many criterias.
    def get(self, table_name):
        pass

    def update(self, table_name):
        pass

    def insert(self, table_name):
        pass

    def delete(self, table_name):
        pass


# Serve as an adapter with the temporary json database.
# Later, we'll use a SQLite adapter/a Postgres adapter.
class JsonDb:
    def __init__(self, table_name):
        self.data = ""

    # For every request, self.get_json_data(table_name). A decorator?
    def get_by_key(self, item_id):
        item_id = str(item_id)
        return self.data[item_id]

    def get_json_data(self, table_name):
        file_path = Path(__file__).parent / f"{table_name}.json"

        with open(file_path, "r") as file:
            return json.load(file)


class SqliteDb():
    pass