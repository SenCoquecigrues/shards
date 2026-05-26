import logging
import sys

from utils.csv_writer import CharacterWriter, DomainWriter, PlaceWriter, PlayerWriter


class CommandHandler:
    def __init__(self):
        if len(sys.argv) > 1:
            match sys.argv[1]:
                case "generate_templates":
                    self.generate_templates()
                case _:
                    logging.error("Commande inconnue")

    def generate_templates(self):
        char_writer = CharacterWriter()
        char_writer.write_csv()

        dom_writer = DomainWriter()
        dom_writer.write_csv()

        place_writer = PlaceWriter()
        place_writer.write_csv()

        player_writer = PlayerWriter()
        player_writer.write_csv()
