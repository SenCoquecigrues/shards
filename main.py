import settings

from db.db_adapter import DbAdapter
from view.commands import CommandHandler
from view.pages import MainPage, WelcomePage


if __name__ == "__main__":
    #db_handler = DbHandler(settings.DB_TYPE, "save")
    #my_account = db_handler.fetch_value("id", 0)
    #page = WelcomePage()

    #page.display_page()
    command_handler = CommandHandler()
    print("Bienvenue dans Éclats")

    #print(my_account)