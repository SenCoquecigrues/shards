from utils.csv_writer import *
from mechanics.db_handler import DbHandler

if __name__ == "__main__":
    db_handler = DbHandler("json", "save")
    my_account = db_handler.fetch_value("id", 0)
    print("Bienvenue dans Éclats")
    print(my_account)