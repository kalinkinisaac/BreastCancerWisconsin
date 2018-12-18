import os
import csv
import sqlite3

CREATE_TABLE_STR = "CREATE TABLE {} (id INTEGER PRIMARY KEY, {});"
LOAD_DATA_STR = "INSERT INTO {} ({}) VALUES ({});"
SELECT_ROW_ID_STR = "SELECT {} FROM {} WHERE id=?"
SELECT_ROW_ID_RANGE_STR = "SELECT {} FROM {} WHERE id>=? AND id <?"
DROP_TABLE_STR = "DROP TABLE IF EXISTS {};"
DIR_PATH = os.path.dirname(os.path.abspath(__file__))


class Database(object):
    def __init__(self, file_name, db_name, fields=None):
        self.name = db_name
        self.conn = sqlite3.connect(os.path.join(DIR_PATH, file_name))
        self.curs = self.conn.cursor()
        self._columns = self.get_columns()

        if fields:
            self.create(fields)
        else:
            self._columns = self.get_columns()

    def create(self, fields):
        self.curs.execute(DROP_TABLE_STR.format(self.name))

        columns_str = ', '.join([f"{field} TEXT" for field in fields])

        self.curs.execute(CREATE_TABLE_STR.format(self.name, columns_str))

        self._columns = self.get_columns()

    def get_columns(self):
        self.curs.execute("PRAGMA table_info({});".format(self.name))
        return list(map(lambda c: c[1], self.curs.fetchall()))[1:]

    def load_data(self, data_path):
        if not self._columns:
            raise Exception('Database has not been initialized')

        reader = csv.reader(open(data_path, 'r'), delimiter=',')
        params = ', '.join(self._columns)
        blanks = ', '.join(['?'] * len(self._columns))

        for row in reader:
            row_str = list(map(str, row))
            self.curs.execute(LOAD_DATA_STR.format(self.name, params, blanks), row_str)

        self.conn.commit()

    def get_row(self, row_id, fields=None):
        self.curs.execute(SELECT_ROW_ID_STR.format(', '.join(list(self._columns if not fields else fields)), self.name),
                          (row_id,))
        return self.curs.fetchall()

    def get_rows(self, row_min_id, row_max_id, fields=None):
        self.curs.execute(
            SELECT_ROW_ID_RANGE_STR.format(', '.join(list(self._columns if not fields else fields)), self.name),
            (row_min_id, row_max_id,))
        return self.curs.fetchall()
