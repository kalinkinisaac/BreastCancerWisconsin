from database import db

class Tutorials:
    @staticmethod
    def get_sample(sample_id):
        query = db.get_row(sample_id)[0]
        return {"inputs" : query[:-1], "answer" : [query[-1]]}
