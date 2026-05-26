import os

from dotenv import load_dotenv, dotenv_values


load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "json") 
DISPLAY_TYPE = os.getenv("DISPLAY_TYPE", "console")