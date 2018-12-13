import csv, sqlite3
conn = sqlite3.connect("db.db")
curs = conn.cursor()
curs.execute("CREATE TABLE PCFC (id INTEGER PRIMARY KEY, identifier INTEGER, clump_thickness INTEGER, "
             "cell_size_uniformity INTEGER, cell_shape_uniformity INTEGER, marginal_adhesion INTEGER,"
             "single_epithelial_cell_size INTEGER, bare_nuclei INTEGER, bland_chromatin INTEGER,"
             "normal_nucleoli INTEGER, mitoses INTEGER, class INTEGER);")
reader = csv.reader(open('data.txt', 'r'), delimiter=',')
for row in reader:
    to_db = list(map(str, row))
    curs.execute("INSERT INTO PCFC (identifier, clump_thickness, cell_size_uniformity, cell_shape_uniformity,"
                 "marginal_adhesion, single_epithelial_cell_size, bare_nuclei, bland_chromatin,"
                 "normal_nucleoli, mitoses, class) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
conn.commit()
