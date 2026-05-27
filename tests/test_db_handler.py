import unittest

from pathlib import Path
from unittest.mock import patch

from db import get_db_path, DbHandler

class TestDbHandler(unittest.TestCase):
    def tearDown(self):
        base_path = Path(__file__).parents[0] / 'sqlite.db'
        try:
            Path.unlink(base_path)
        except:
            pass

    def test_crash_if_table_miss(self):
        with self.assertLogs(level='CRITICAL') as context_manager:
            with patch(
                'db.get_db_path',
                return_value=Path(__file__).parents[0] / 'sqlite.db'
            ):
                with self.assertRaises(ConnectionError):
                    db_handler = DbHandler()
                    db_handler.check_tables_integrity()

        self.assertTrue(
            context_manager.output[0].startswith(
                "CRITICAL:root:Missing tables: ["
            )
        )       

    def test_crash_if_tables_dont_fit_models(self):
        #TODO: implement later
        pass 