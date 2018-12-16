from database import db

# TODO: move this code to another place
# This is just example of db usage

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

# This code will create database file in root directory of the project
db.init(fields=fields)
db.load_data("data.txt")


