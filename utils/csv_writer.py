import csv, logging
from pathlib import Path

from .global_constants import GlobalConstants


"""
    Template class for other CSV handlers.
    Indicate expected return types.
"""
class CsvHandler:
    def __init__(self):
        self.header = self.get_header()
        self.template_title = ""

    def write_csv(self, file_folder="template_files") -> None:
        csv_file_path = self.get_template_file_path(file_folder)

        try:
            with open(csv_file_path, 'w', newline='') as csvfile:
                file_writer = csv.writer(csvfile, delimiter=';')
                file_writer.writerow(self.header)
        except Exception as e:
            logging.error(f'Error while creating {self.template_title}: {e}')

    def get_dicts_from_csv(self, file_name):
        file_path = self.get_import_file_path(file_name)

        if not Path(file_path).exists():
            error_msg = f"Could not find import_files/{file_name}. Is the file in the directory?"
            raise FileNotFoundError(error_msg)

        try:
            with open(file_path, 'r', newline='') as csvfile:
                file_reader = csv.reader(csvfile, delimiter=';')
                file_reader = self.format_reader_result(file_reader)
                header = file_reader[0]

                if not self.header_is_consistent(header):
                    raise Exception(f"Wrong header for {file_path}")

                file_reader.pop(0)
                return [
                    self.format_row_into_dict(header, entry) for entry in file_reader
                ]

        except Exception as e:
            error_msg = f'Error while importing from {self.template_title}: {e}'
            logging.error(error_msg)
        
        # return dict to main
        # from main: check if dict is in json
        # if not, then save it THEN add it to json
        # If not: log the error and the object name (ideally the file number?)
        # Log success as well
        # Rename file to avoid re-import
        # This should be extensively tested

    ################# VARIOUS UTILS
    def format_reader_result(self, reader_obj) -> list[list]:
        return [row for row in reader_obj if len(row) > 0]

    def format_row_into_dict(self, header: list, row: list) -> dict:
        loop_range = range(len(header))
        final_dict = {}
        for i in loop_range:
            final_dict.update({header[i]: row[i]})
        return final_dict

    def header_is_consistent(self, imported_csv_header: list):
        if self.header == imported_csv_header:
            return True
        return False

    def get_import_file_path(self, file_name: str) -> str:
        folder = Path(__file__).parents[1] / "utils/import_files"

        if not file_name.endswith(".csv"):
            file_name = f"{file_name}.csv"

        return folder / file_name

    def get_template_file_path(self, folder_name: str) -> str:
        folder = Path(__file__).parent / folder_name
        return folder / f"{self.template_title}.csv"

    def get_header(self) -> list[str]:
        pass


class CharacterCsvHandler(CsvHandler):
    def __init__(self):
        super().__init__()
        self.template_title = 'char_template'

    def get_header(self):
        character_traits = GlobalConstants.CHAR_TRAITS
        result = GlobalConstants.CHAR_BASE_ATTRIBUTES

        for facets_list in character_traits.keys():
            result.extend(character_traits[facets_list])

        return result


class DomainCsvHandler(CsvHandler):
    def __init__(self):
        super().__init__()
        self.template_title = 'dom_template'

    def get_header(self):
        return GlobalConstants.DOMAIN_BASE_ATTRIBUTES


class PlaceCsvHandler(CsvHandler):
    def __init__(self):
        super().__init__()
        self.template_title = 'place_template'

    def get_header(self):
        return GlobalConstants.OBJ_BASE_ATTRIBUTES


class PlayerCsvHandler(CsvHandler):
    def __init__(self):
        super().__init__()
        self.template_title = 'player_template'

    def get_header(self):
        return GlobalConstants.OBJ_BASE_ATTRIBUTES


def return_proper_csvhandler(file_name):
    if file_name.startswith("char_"):
        return CharacterCsvHandler()
    elif file_name.startswith("dom_"):
        return DomainCsvHandler()
    elif file_name.startswith("place_"):
        return PlaceCsvHandler()
    elif file_name.startswith("player_"):
        return PlayerCsvHandler()
    else:
        raise AttributeError(f"{file_name} name not handled.")