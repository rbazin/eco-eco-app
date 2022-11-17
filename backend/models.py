from . import db
from flask_login import UserMixin
from sqlalchemy_utils import ScalarListType, JSONType

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class UserData(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    droplets=db.Column(db.Integer)
    streak=db.Column(db.Integer)
    challenge=db.Column(db.Integer)
    badges= db.Column(ScalarListType(int))
    favs= db.Column(ScalarListType(int))
    stats=db.Column(JSONType)

class Challenges(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    task= db.Column(db.String(200))
    mode= db.Column(db.String(100))
    place= db.Column(db.String(100))
    droplets= db.Column(db.Integer)

    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "task": self.task,
            "mode": self.mode,
            "place": self.place,
            "droplets": self.droplets
        }






