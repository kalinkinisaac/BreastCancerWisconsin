import sqlite3

DB_PATH = "db2.db"
DB_NAME = "WDBC" # Wisconsin Diagnostic Breast Cancer

conn = sqlite3.connect(DB_PATH)
curs = conn.cursor()

from .database import Database

fields = dict({
    "identifier" : "INTEGER",
    "clump_thickness" : "INTEGER",
    "cell_size_uniformity" : "INTEGER",
    "cell_shape_uniformity" : "INTEGER",
    "marginal_adhesion" : "INTEGER",
    "single_epithelial_cell_size" : "INTEGER",
    "bare_nuclei" : "INTEGER",
    "bland_chromatin" : "INTEGER",
    "normal_nucleoli" : "INTEGER",
    "mitoses" : "INTEGER",
    "class" : "INTEGER"
})

db = Database(fields=fields)

__all__ = ['db']