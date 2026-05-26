import json

from pathlib import Path

# Serve as an adapter with the temporary json database.
# Later, we'll use a SQLite adapter/a Postgres adapter.
class JsonSaveAdapter:
    def __init__(self, table_name):
        self.data = self.get_json_data(table_name)

    def get_by_id(self, item_id):
        item_id = str(item_id)
        return self.data[item_id]

    def get_json_data(self, table_name):
        file_path = Path(__file__).parent / f"{table_name}.json"

        with open(file_path, "r") as file:
            return json.load(file)
