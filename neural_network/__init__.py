from database import db
import numpy as np
# TODO: move this code to another place
# This is just example of db usage

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

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


