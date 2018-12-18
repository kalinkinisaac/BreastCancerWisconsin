from database import db

FIELDS = ["identifier", "clump_thickness", "cell_size_uniformity", "cell_shape_uniformity", "marginal_adhesion",
          "single_epithelial_cell_size", "bare_nuclei", "bland_chromatin", "normal_nucleoli", "mitoses", "class"]

if __name__ == "__main__":
    db.create(FIELDS)
    db.load_data('data.txt')