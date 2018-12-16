import sqlite3

DB_PATH = "db2.db"
DB_NAME = "WDBC" # Wisconsin Diagnostic Breast Cancer

conn = sqlite3.connect(DB_PATH)
curs = conn.cursor()

from .database import Database

db = Database()

__all__ = ['db']