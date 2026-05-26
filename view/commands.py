import logging, os, subprocess, sys

from utils.csv_writer import CharacterWriter, DomainWriter, PlaceWriter, PlayerWriter


class CommandHandler:
    def __init__(self):
        if len(sys.argv) > 1:
            match sys.argv[1]:
                case "generate_templates":
                    self.generate_templates()
                case "tests":
                    self.run_tests()
                case _:
                    logging.error("Commande inconnue")

            os._exit(1)

    def generate_templates(self):
        char_writer = CharacterWriter()
        char_writer.write_csv()

        dom_writer = DomainWriter()
        dom_writer.write_csv()

        place_writer = PlaceWriter()
        place_writer.write_csv()

        player_writer = PlayerWriter()
        player_writer.write_csv()

    """
        Command format:
            python main.py tests
            python main.py module_name
            python main.py module_name.function_name
    """
    def run_tests(self):
        try:
            if len(sys.argv) == 2:
                subprocess.run(
                    'python -m unittest tests',
                    shell=True,
                    executable="/bin/bash"
                )
            elif len(sys.argv) == 3:
                subprocess.run(
                    self.handle_multi_part_test_path(sys.argv[2]),
                    shell=True,
                    executable="/bin/bash"
                )
            else:
                raise ValueError("Test command only take one argument. Please check README.")

        except Exception as e:
            logging.error(e)

    ######## UTILS FUNCTIONS
    def handle_multi_part_test_path(self, arg):
        if not "." in arg:
            return f"python -m unittest tests.{arg}"
        else:
            arg = arg.split(".")
            module_name = arg[0]
            function_name = arg[1]
            class_name = ''.join(word.capitalize() for word in module_name.split('_'))

            return f"python -m unittest tests.{module_name}.{class_name}.{function_name}"