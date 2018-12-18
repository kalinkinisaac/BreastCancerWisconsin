from database import db

class Tutorials:
    @staticmethod
    def get_sample(sample_id):
        query = db.get_row(sample_id)
        return query[0][2::]
