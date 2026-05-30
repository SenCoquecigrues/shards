import inspect, json, logging, sqlite3

from pathlib import Path

import settings
from db import serialisers, fields

def get_db_path():
    return Path(__file__).parents[0] / 'sqlite.db'

class SqlDbHandler:
    list_of_used_serialisers = serialisers.get_all_serialisers()

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

    def check_tables_integrity(self) -> None:
        # TODO: later on, check that table = Serialiser template

        list_of_missing_tables = [ser.table_name for ser in self.serialisers_missing_table()]
        
        if len(list_of_missing_tables) > 0:
            logging.critical(f"Missing tables: {list_of_missing_tables}")
            raise ConnectionRefusedError("Missing tables: please see logs.")

    def create_tables_if_not_exist(self) -> None:
        orphan_serialisers = self.serialisers_missing_table()
        file_path = Path(__file__).parent / f"field_type_to_{settings.DB_TYPE}_type.json"
        equivalences = {}

        with open(file_path, "r") as data:
            equivalences = json.load(data)

        for ser in orphan_serialisers:
            self.create_table(ser, equivalences)
            
    # TODO: move into a better place
    def get_sql_line(self, field, equivalences):
        field = list(field.values())[0]
        column_name = field.field_name
        data_type = equivalences[field.sql_datatype]
        is_unique = "UNIQUE" if field.is_unique else ""

        if field.sql_datatype in ("TEXT", "LONG_TEXT") and settings.DB_TYPE != "sqlite":
            return f"{column_name} {data_type} NOT NULL {is_unique}"
        return f"{column_name} {data_type} NOT NULL {is_unique}"

    # TODO: move into a better place
    def get_serialisers_fields(self, instance):
        serialisers_fields = []
        for attr_name, attr_value in instance.__dict__.items():
            if isinstance(attr_value, fields.BaseField):
                serialisers_fields.append({attr_name: attr_value})
        
        return serialisers_fields

    @db_access_wrapper
    def create_table(
        self,
        conn,
        ser: serialisers.BaseSerialiser,
        equivalences: dict,
        ) -> None:
        conn.set_trace_callback(print)

        instance = ser(reference="REF", name="name", element="element", level=1)
        fields = self.get_serialisers_fields(instance)
        sql_lines = []
        id_line = ""

        if settings.DB_TYPE == "sqlite":
            id_line = "id INTEGER PRIMARY KEY AUTOINCREMENT"
        else:
            id_line = "id INT AUTO_INCREMENT PRIMARY KEY"

        for field in fields:
            sql_lines.append(self.get_sql_line(field, equivalences))

        sql_lines = ",\n".join(sql_lines)

        req = f"""
            CREATE TABLE IF NOT EXISTS {ser.table_name} (
                {id_line},
                {sql_lines}
        );
        """

        conn.cursor().execute(req)
    
        return conn.commit()

    @db_access_wrapper
    def serialisers_missing_table(self, conn) -> list:
        cursor = conn.cursor()
        list_of_serialisers = SqlDbHandler.list_of_used_serialisers
        serialisers_missing_table = []

        for serialiser in list_of_serialisers:
            # TODO: Sen: check this out; it doesn't work
            table_exists = self.table_exists(cursor, serialiser.table_name)
            if not table_exists:
                serialisers_missing_table.append(serialiser)

        return serialisers_missing_table

    def table_exists(self, cursor, table_name: str):
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        return cursor.fetchone() is not None

    def check_serialisers_coherent_with_db(self):
        results = []

        for name, obj in inspect.getmembers(serialisers):
            if (
                inspect.isclass(obj) and
                obj.__name__.endswith("Serialiser") and
                not obj == serialisers.BaseSerialiser
            ):
                results.append(
                    self.check_serialiser_coherent_with_table(obj)
                )

        return results
        # For each serialiser, get all fields
        # Get the table with the table_name name
        # Get all its columns
        # Check that the column list and field name list are the same
        pass

    def check_serialiser_coherent_with_table(self, serialiser):
        # TODO - incomplete
        all_fields = serialiser.__static_attributes__
        
        print(serialiser.table_name)
        print(serialiser.__static_attributes__)

    def get(self, table_name):
        pass

    def update(self, table_name):
        pass

    def insert(self, table_name):
        pass

    def delete(self, table_name):
        pass


class ModelSqlHandler(SqlDbHandler):
    pass