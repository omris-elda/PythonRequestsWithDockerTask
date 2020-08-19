from app import db

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    animal_name = db.Column(db.String(50), index = True, unique = True)
    animal_noise = db.Column(db.String(50), index = True)