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


class SqliteDb():
    def __init__(self):
        con = sqlite3.connect("sqlite.db")
