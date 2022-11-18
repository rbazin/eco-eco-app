from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user
from flask_cors import cross_origin
from . import app
from . import db
from .models import User, UserData, Challenges, Facts
import json, os, random


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


def data_loading():
    # Challenges

    with app.app_context():
        db.session.query(Challenges).delete()
        db.session.commit()
        db.session.query(Facts).delete()
        db.session.commit()

    f = open(str(os.path.dirname(os.path.abspath(__file__))) + "/data/challenges.json")
    data = json.load(f)
    for i in data:
        x = Challenges(
            task=i["Task"], mode=i["Mode"], place=i["Place"], droplets=i["Droplets"]
        )
        with app.app_context():
            db.session.add(x)
            db.session.commit()
    f = open(str(os.path.dirname(os.path.abspath(__file__))) + "/data/facts.json")
    data = json.load(f)
    for i in data:
        x = Facts(mode=i["Mode"], fact=i["Fact"])
        with app.app_context():
            db.session.add(x)
            db.session.commit()
    return


def dict_helper(objlist):
    result = [item.obj_to_dict() for item in objlist]
    return result


data_loading()


@app.route("/api/login", methods=["POST", "GET"])
@cross_origin()
def login():
    response_object = {"status": "success"}
    if request.method == "POST":
        data = request.get_json()
        name = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(name=name).first()

        if not user or not check_password_hash(user.password, password):
            return jsonify(
                "Login unsuccessful!"
            )  # if user doesn't exist or password is wrong, reload the page

        else:
            login_user(user)
            user_data = UserData.query.get(user.id)
            response_object["userId"] = user.id
            response_object["userName"] = user.name
            response_object["userDroplets"] = user_data.droplets
            response_object["userStreak"] = user_data.streak
            return jsonify(response_object)
    else:
        return {"status": "fail"}


@app.route("/api/signup", methods=["POST", "GET"])
@cross_origin()
def signup():
    response_object = {"status": "success"}
    if request.method == "POST":
        data = request.get_json()
        name = data.get("username")
        password = data.get("password")
        user = User.query.filter_by(name=name).first()

        if (
            user
        ):  # if a user is found, we want to redirect back to signup page so user can try again
            return {"success": False}

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(
            name=name, password=generate_password_hash(password, method="sha256")
        )

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter_by(name=name).first()
        user_data = UserData(id=user.id, droplets=0, streak=0, challenge=0)
        db.session.add(user_data)
        db.session.commit()
        response_object["success"] = True
        response_object["userId"] = user.id
        response_object["userName"] = user.name
        response_object["userDroplets"] = user_data.droplets
        response_object["userStreak"] = user_data.streak
        return response_object
    else:
        return {"success": False}


@app.route("/api/questionnaire_1", methods=["POST", "GET"])
@cross_origin()
def questionnnaire1():
    response_object = {"status": "success"}
    if request.method == "POST":
        data = request.get_json()
        user_data = UserData.query.get(data["userId"])
        user_data.modes = data["meansOfTransport"]
        db.session.commit()
        return response_object
    else:
        return {"status": "fail"}


@app.route("/api/questionnaire_2", methods=["POST", "GET"])
@cross_origin()
def questionnnaire2():
    response_object = {"status": "success"}
    if request.method == "POST":
        data = request.get_json()
        user_data = UserData.query.get(data["userId"])
        places = {"daily": [], "weekly": [], "monthly": []}
        for i in range(len(data["frequenciesOfPlaces"])):
            if data["frequenciesOfPlaces"][i]["frequency"]:
                places[data["frequenciesOfPlaces"][i]["frequency"]].append(
                    data["frequenciesOfPlaces"][i]["mean"]
                )
        user_data.places = places
        db.session.commit()
        # print(UserData.query.get(data.userId))
        return response_object
    else:
        return {"status": "fail"}

@app.route('/api/challenge/complete', methods=['POST', 'GET'])
@cross_origin()
def challenge_complete():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data=request.get_json()
        user_id=data['userId']
        user_data=UserData.query.get(user_id)
        challenges=Challenges.query.get(user_data.challenge)
        user_data.droplets+=challenges.droplets
        user_data.streak+=1
        user_data.challenge=0
        response_object['userDroplets']=user_data.droplets
        response_object['streak']=user_data.streak
        db.session.commit()
        return response_object
    else:
        return {'status': 'fail'}

@app.route('/api/challenge/abort', methods=['POST', 'GET'])
@cross_origin()
def challenge_abort():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data=request.get_json()
        user_id=data['userId']
        user_data=UserData.query.get(user_id)
        user_data.challenge=0
        user_data.streak=0
        db.session.commit()
        response_object["userStreak"] = 0
        return response_object


@app.route("/api/challenges", methods=["POST", "GET"])
@cross_origin()
def challenges_basic():
    response_object = {"status": "success"}
    challenge_ids = [random.choice(list(range(2, 12))) for x in range(3)]
    challenge_list = []
    for i in range(len(challenge_ids)):
        challenge = Challenges.query.get(challenge_ids[i])
        fact = Facts.query.filter_by(mode=challenge.mode).first()
        challenge_list.append(
            {
                "id": challenge.id,
                "title": challenge.task,
                "droplets": challenge.droplets,
                "fact": fact.fact,
            }
        )
    response_object["challenges"] = challenge_list
    return response_object

@app.route('/api/accept_challenge', methods=['POST', 'GET'])
@cross_origin()
def challenge_select():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data=request.get_json()
        user_id=data['userId']
        challenge_id=data['challengeId']
        user_data=UserData.query.get(user_id)
        user_data.challenge=challenge_id
        db.session.commit()
        response_object['success']= True
        return response_object
