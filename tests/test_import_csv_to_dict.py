import csv, os, unittest

from pathlib import Path
from shutil import rmtree
from unittest.mock import patch

from utils import csv_writer
from view import CommandHandler


class TestImportCsvToDisc(unittest.TestCase):
    def setUp(self):
        # Set up a test_import_file rather than using the real
        # one, so test datas won't get polluted.
        base_folder = Path(__file__).parents[1] / "utils"
        test_folder_path = base_folder / "test_import_files"
        os.makedirs(test_folder_path, exist_ok=True)

        domain_csv_handler = csv_writer.DomainCsvHandler()
        domain_csv_handler.write_csv(file_folder="test_import_files")

    def tearDown(self):
        base_folder = Path(__file__).parents[1] / "utils"
        test_folder_path = base_folder / "test_import_files"
        rmtree(test_folder_path)

    # Get our test files folder/files easily
    def get_test_file_path(self, file_name="dom_template.csv") -> str:
        base_folder = Path(__file__).parents[1] / "utils"
        return base_folder / f"test_import_files/{file_name}"

    def test_crashes_if_wrong_file_name_format(self):
        args = ['main.py', 'import', 'does_not_exists']
        command_handler = CommandHandler(is_test=True)

        with self.assertRaises(AttributeError):
            command_handler.import_objects_from_csv(args)

    def test_crashes_if_csv_file_does_not_exists(self):
        args = ['main.py', 'import', 'dom_does_not_exists']
        command_handler = CommandHandler(is_test=True)

        with self.assertRaises(FileNotFoundError):
            command_handler.import_objects_from_csv(args)

    def test_crashes_if_header_is_not_right(self):
        file_path = self.get_test_file_path()

        with open(file_path, 'w', newline='') as csvfile:
            file_writer = csv.writer(csvfile, delimiter=';')
            file_writer.writerow("wrong;values;alas")

        with self.assertLogs(level='ERROR') as context_manager:
            with patch(
                'utils.csv_writer.CsvHandler.get_import_file_path',
                return_value=file_path
            ):
                csv_handler = csv_writer.DomainCsvHandler()
                csv_handler.get_dicts_from_csv(file_path)
                self.assertTrue(
                    context_manager.output[0].startswith(
                        "ERROR:root:Error while importing from dom_template: Wrong header"
                    )
                )

    def test_get_dict_from_proper_csv_file(self):
        file_path = self.get_test_file_path()

        with open(file_path, 'a', newline='') as csvfile:
            file_writer = csv.writer(csvfile, delimiter=';')
            file_writer.writerow(["MY_TEST_DOMAIN", "My test domain", "FORBIDDEN", 2])
            file_writer.writerow(["MY_TEST_DOMAIN 2", "My test domain 2", "FORBIDDEN", 1])

        with self.assertNoLogs(level='ERROR') as context_manager:
            with patch(
                'utils.csv_writer.CsvHandler.get_import_file_path',
                return_value=file_path
            ):
                csv_handler = csv_writer.DomainCsvHandler()
                instance_dicts = csv_handler.get_dicts_from_csv(file_path)
                projected_result = {
                    "reference": "MY_TEST_DOMAIN",
                    "name": "My test domain",
                    "element": "FORBIDDEN",
                    "level": '2'
                }
                self.assertTrue(len(instance_dicts) == 2)
                self.assertEqual(instance_dicts[0], projected_result)
