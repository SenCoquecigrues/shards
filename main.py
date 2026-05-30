import settings

from db import DbHandler
from view.commands import CommandHandler
from view.text_screens import MainScreen, WelcomeScreen
from utils.global_constants import GlobalConstants

if __name__ == "__main__":
    command_handler = CommandHandler()

    screen_displayer = None
    db_handler = DbHandler()

    if settings.DISPLAY_TYPE in GlobalConstants.TEXT_DISPLAYS:
        screen_displayer = WelcomeScreen()
    else:
        raise ValueError("Incorrect display type.")

    if settings.TABLE_INITIALISATION == GlobalConstants.MANUAL_MODE:
        db_handler.check_tables_integrity()
    else:
        db_handler.create_tables_if_not_exist()
    screen = WelcomeScreen()
    screen.display_screen()
    #page.display_screen()
    #my_account = db_handler.fetch_value("id", 0)
    # from rich import print
    # print("[bold blue encircle]alert![/bold blue italic]")
    # print("[bold italic yellow on red blink]This text is impossible to read")
    # print("Bienvenue dans Éclats")
    #print(my_account)