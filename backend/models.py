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






