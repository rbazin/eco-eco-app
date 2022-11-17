from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user
from flask_cors import cross_origin
from backend import app
from backend import db
from backend.models import User, UserData, Challenges
import json, os


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


def mark_challenge_complete(user_id):
    user_data=UserData.query.get(user_id)
    user_data.challenge=0
    db.session.commit()
    return

##Methods

def data_loading():
    #Challenges
    f = open(str(os.path.dirname(os.path.abspath(__file__)))+'/data/challenges.json')
    data = json.load(f)
    with app.app_context():
        db.session.query(Challenges).delete()
        db.session.commit()

    for i in data:
        x=Challenges(task= i['Task'], mode= i['Mode'], place= i['Place'], droplets= i['Droplets'])
        with app.app_context():
            db.session.add(x)
            db.session.commit()
    return

def dict_helper(objlist):
    result = [item.obj_to_dict() for item in objlist]
    return result

data_loading()

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

@app.route("/")
def home():
    #return("Home")
    return(jsonify(challenges=dict_helper(Challenges.query.all())))

@app.route("/api/login", methods=['POST', 'GET'])
@cross_origin()
def login():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data=request.get_json()
        name = data.get('username')
        password = data.get('password')


        user = User.query.filter_by(name=name).first()

        if not user or not check_password_hash(user.password, password):
            return jsonify("Login unsuccessful!") # if user doesn't exist or password is wrong, reload the page


        else:
            login_user(user)
            user_data=UserData.query.get(user.id)
            response_object['userId']=user.id
            response_object['userName']=user.name
            response_object['userDroplets']=user_data.droplets
            response_object['userStreak']=user_data.streak
            return jsonify(response_object)


@app.route('/api/signup', methods=['POST', 'GET'])
@cross_origin()
def signup():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data=request.get_json()
        name = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(name=name).first()

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            return jsonify("User already exists!")

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(name=name, password=generate_password_hash(password, method='sha256'))


        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter_by(name=name).first()
        user_data=UserData(id=user.id, droplets=0, streak=0, challenge=0)
        db.session.add(user_data)
        db.session.commit()

    return response_object
