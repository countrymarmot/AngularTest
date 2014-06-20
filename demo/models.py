from demo import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    nation = db.Column(db.String(10))
    club = db.Column(db.String(10))
