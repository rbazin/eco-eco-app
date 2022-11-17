from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})# CORS allowed for all domains on all routes

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

from backend.models import User, UserData, Challenges


with app.app_context():
    db.create_all()



from backend import main


if __name__=="__init__":
    app.run(debug=True)
    #User.__table__.drop(db.engine)
    #UserData.__table__.drop(db.engine)
    #Challenges.__table__.drop(db.engine)

