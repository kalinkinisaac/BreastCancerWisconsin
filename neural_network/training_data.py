from database import db

FIELDS = ["clump_thickness", "cell_size_uniformity", "cell_shape_uniformity", "marginal_adhesion",
          "single_epithelial_cell_size", "bare_nuclei", "bland_chromatin", "normal_nucleoli", "mitoses", "class"]

def input_normaliser(x):
    return float(x) / 10

def answer_normaliser(x):
    return float(x) / 4

class Tutorials:
    @staticmethod
    def get_sample(sample_id):
        query = db.get_row(sample_id, fields=FIELDS)[0]

        if '?' in query:
            raise ValueError('Missing data sample')

        return {"inputs": list(map(input_normaliser, query[:-1])), "answer": [answer_normaliser(query[-1])]}

    @staticmethod
    def get_samples(id_min=1, id_max=500):
        query = list(filter(lambda r: '?' not in r, db.get_rows(id_min, id_max, fields=FIELDS)))
        inputs, answers = [], []

        for row in query:
            inputs += [list(map(input_normaliser, row[:-1]))]
            answers += [answer_normaliser(row[-1][0])]

        return inputs, answers
