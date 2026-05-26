import csv
import logging
from pathlib import Path

from .global_constants import GlobalConstants

"""
    Template class for other CSV handlers.
    Indicate expected return types.
"""
class CsvWriter:
    def __init__(self):
        self.header = self.get_header()
        self.title = ""

    def write_csv(self) -> None:
        folder = Path(__file__).parent / "import_files"
        file_path = folder / f"{self.title}.csv"

        try:
            with open(file_path, 'w', newline='') as csvfile:
                file_writer = csv.writer(csvfile, delimiter=';')
                file_writer.writerow(self.header)
        except Exception as e:
            logging.error(f'Error while creating {self.title}: {e}')

    def import_from_csv(self):
        pass

    def get_header(self) -> list[str]:
        pass


class CharacterWriter(CsvWriter):
    def __init__(self):
        super().__init__()
        self.title = 'char_template'

    def get_header(self):
        character_traits = GlobalConstants.CHAR_TRAITS
        result = GlobalConstants.CHAR_BASE_ATTRIBUTES

        for facets_list in character_traits.keys():
            result.extend(character_traits[facets_list])

        return result


class DomainWriter(CsvWriter):
    def __init__(self):
        super().__init__()
        self.title = 'dom_template'

    def get_header(self):
        return GlobalConstants.DOMAIN_BASE_ATTRIBUTES


class PlaceWriter(CsvWriter):
    def __init__(self):
        super().__init__()
        self.title = 'place_template'

    def get_header(self):
        return GlobalConstants.OBJ_BASE_ATTRIBUTES


class PlayerWriter(CsvWriter):
    def __init__(self):
        super().__init__()
        self.title = 'place_template'

    def get_header(self):
        return GlobalConstants.OBJ_BASE_ATTRIBUTES
