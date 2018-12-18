from .database import Database

db = Database(file_name="db2.db", db_name="WDBC")

__all__ = ['db']
