from database import db


class Tutorials:
    @staticmethod
    def get_sample(sample_id):
        query = db.get_row(sample_id)[0]
        if '?' in query:
            raise ValueError('idi nahuy')

        return {"inputs": list(map(lambda x: x / 10, query[:-1])), "answer": [query[-1] / 4]}

    @staticmethod
    def get_samples(id_min=1, id_max=500):
        query = list(filter(lambda r: '?' not in r, db.get_rows(id_min, id_max)))
        inputs, answers = [], []
        for row in query:
            inputs += [list(map(lambda x: x / 10, row[:-1]))]
            answers += [row[-1] / 4]
        return inputs, answers
