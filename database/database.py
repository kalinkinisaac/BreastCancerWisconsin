import csv
from . import curs, conn, DB_NAME

class Database(object):
    def __init__(self):
        self._fields = None

    def init(self, fields):
        self._fields = fields
        self._create_db()

    def _create_db(self):
        if not self._fields:
            raise Exception('Database have not been initialized')

        fields_str = ', '.join(["{} {}".format(x, y) for (x, y) in zip(self._fields.keys(), self._fields.values())])
        curs.execute("CREATE TABLE {} (id INTEGER PRIMARY KEY, {});".format(DB_NAME, fields_str))

    def load_data(self, data_path):
        if not self._fields:
            raise Exception('Database have not been initialized')

        reader = csv.reader(open(data_path, 'r'), delimiter=',')
        fields_str_1 = ', '.join(self._fields.keys())
        fields_str_2 = ', '.join(['?'] * len(self._fields))

        for row in reader:
            to_db = list(map(str, row))
            curs.execute("INSERT INTO {} ({}) VALUES ({});".format(DB_NAME, fields_str_1, fields_str_2), to_db)

        conn.commit()