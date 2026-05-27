from settings import DB_TYPE

if DB_TYPE == "sqlite":
    from .db_handler import get_db_path, SqlDbHandler as DbHandler
else:
    errorMsg = f"Unknown database type : {DB_TYPE}"
    raise ValueError()