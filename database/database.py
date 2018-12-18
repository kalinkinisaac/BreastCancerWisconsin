import csv, sqlite3

class Database(object):
    def __init__(self, file_path="db2.db", name='WDBC'):
        self._fields = None
        self.name = name
        self.conn = sqlite3.connect(file_path)
        self.curs = self.conn.cursor()

    def create(self, fields):
        self._fields = fields
        self._create()

    def _create(self):
        if not self._fields:
            raise Exception('Database have not been initialized')

        fields_str = ', '.join(["{} {}".format(x, y) for (x, y) in zip(self._fields.keys(), self._fields.values())])
        self.curs.execute("CREATE TABLE {} (id INTEGER PRIMARY KEY, {});".format(self.name, fields_str))

    def load_data(self, data_path):
        if not self._fields:
            raise Exception('Database have not been initialized')

        reader = csv.reader(open(data_path, 'r'), delimiter=',')
        fields_str_1 = ', '.join(self._fields.keys())
        fields_str_2 = ', '.join(['?'] * len(self._fields))

        for row in reader:
            to_db = list(map(str, row))
            self.curs.execute("INSERT INTO {} ({}) VALUES ({});".format(DB_NAME, fields_str_1, fields_str_2), to_db)

        self.conn.commit()

    def get_row(self, id):
        self.curs.execute("SELECT * FROM {} WHERE id=?".format(self.name), (id,))
        return self.curs.fetchall()

    def get_rows(self, id_min, id_max):
        self.curs.execute("SELECT * FROM {} WHERE id>=? AND id <?".format(self.name), (id_min, id_max,))
        return self.curs.fetchall()