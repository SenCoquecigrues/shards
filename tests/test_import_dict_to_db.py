
# TODO
# TEST3 : block if entry already exists
# TEST3-2 (later?): block if data check fails regarding fields

# if not, then save it
# If not: log the error and the object name (ideally the file number?)
# Log success as well
# Rename file to avoid re-import
# This should be extensively tested
import csv, os, unittest

from pathlib import Path
from shutil import rmtree
from unittest.mock import patch

from utils import csv_writer
from view import CommandHandler


class TestImportCsvToDisc(unittest.TestCase):
    def test_is_true(self):
        self.assertEqual(1, 1)