import logging, os, subprocess, sys

from pathlib import Path

from utils.csv_writer import CharacterCsvHandler, DomainCsvHandler, PlaceCsvHandler, PlayerCsvHandler, return_proper_csvhandler


class CommandHandler:
    def __init__(self, is_test=False):
        # So that it won't get stuck if we call a command for testing.
        if is_test:
            return None

        if len(sys.argv) > 1:
            match sys.argv[1]:
                case "import":
                    self.import_objects_from_csv(sys.argv)
                case "generate_tables":
                    self.generate_tables()
                case "generate_templates":
                    self.generate_templates()
                case "tests":
                    self.run_tests()
                case _:
                    logging.error("Commande inconnue")

            os._exit(1)

    def import_objects_from_csv(self, args):
        #TODO: remember that you still have to finish this once db's ready!
        if len(args) == 2:
            raise AttributeError("Please indicate which file to import.")

        file_name = args[2]
        csv_writer = return_proper_csvhandler(file_name)
        instances_dict = csv_writer.get_dicts_from_csv(file_name)

    def generate_tables(self):
        # TODO: generate tables from serialisers
        pass

    def generate_templates(self):
        char_writer = CharacterCsvHandler()
        char_writer.write_csv()

        dom_writer = DomainCsvHandler()
        dom_writer.write_csv()

        place_writer = PlaceCsvHandler()
        place_writer.write_csv()

        player_writer = PlayerCsvHandler()
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