from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user
from flask_cors import cross_origin
from . import app
from . import db
from .models import User, UserData, Challenges, Facts, Badges
import json, os, random, time, base64
from sqlalchemy.orm.attributes import flag_modified
#import seaborn as sns


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


##Methods
def draw_weekly():
    return
    
def draw_monthly():
    return

def update_stats(user_data, challenge):
    label=time.strftime("%d-%m-%Y")
    if user_data.stats==None:
        user_data.stats={}
    if label not in user_data.stats:
        user_data.stats[label]={
            "Walking":0,
            "Buses":0,
            "Car":0,
            "Subway":0,
            "Bike":0,
            "Trains":0
        }
    user_data.stats[label][challenge.mode]+=1
    return user_data

def update_badges(user_data, challenges):
    badges=Badges.query.all()
    for badge in badges:
        if badge.id not in user_data.badges:
            if badge.criteria=="droplets":
                if user_data.droplets>int(badge.condition):
                    user_data.badges.append(badge.id)
            elif badge.criteria=="streak":
                if user_data.streak>int(badge.condition):
                    user_data.badges.append(badge.id)
            elif badge.criteria=="friends":
                if len(user_data.friends)>int(badge.condition):
                    user_data.badges.append(badge.id)
            elif badge.criteria=="challenge":
                if challenges.mode==badge.condition:
                    user_data.badges.append(badge.id)
            else:
                print("Unknown badge error!")
    return user_data

def commit_data(data):
    with app.app_context():
        db.session.add(data)
        db.session.commit()
    return

def data_loading():
    # Challenges
    with app.app_context():
        db.session.query(Challenges).delete()
        db.session.commit()
        db.session.query(Facts).delete()
        db.session.commit()
        db.session.query(Badges).delete()
        db.session.commit()

        f = open(str(os.path.dirname(os.path.abspath(__file__))) + "/data/challenges.json")
        data = json.load(f)
        for i in data:
            x = Challenges(task=i["Task"], mode=i["Mode"], place=i["Place"], droplets=i["Droplets"])
            commit_data(x)
        f = open(str(os.path.dirname(os.path.abspath(__file__))) + "/data/facts.json")
        data = json.load(f)
        for i in data:
            x = Facts(mode=i["Mode"], fact=i["Fact"])
            commit_data(x)
        f = open(str(os.path.dirname(os.path.abspath(__file__))) + "/data/friends.json")
        data = json.load(f)
        for i in data:
            user = User.query.filter_by(name=i["name"]).first()
            if not (user):
                new_user = User(name=i["name"], password=generate_password_hash(i["password"], method="sha256"))
                commit_data(new_user)
                user = User.query.filter_by(name=i["name"]).first()
                user_data = UserData(id=user.id, droplets=i["droplets"], streak=i["streak"], challenge=i["challenge"], badges=i["badges"], modes=["Walking", "Buses", "Car", "Subway", "Bike", "Trains"])
                user_data.stats={}
                for s in i["stats"]:
                    for key in s:
                        user_data.stats[key]=s[key]
                commit_data(user_data)
        f = open(str(os.path.dirname(os.path.abspath(__file__))) + "/data/badges.json")
        data = json.load(f)
        for i in data:
            x = Badges(badge=i["Badge"], criteria=i["Criteria"], condition=str(i["Condition"]))
            commit_data(x)

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
    return("Home")
    #return(jsonify(challenges=dict_helper(Challenges.query.all())))

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
            response_object['success']= True
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
        user_data = UserData(id=user.id, droplets=0, streak=0, challenge=1, friends=[(User.query.filter_by(name="Leonie").first()).id], badges=[])
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
        response_object['success']= True
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
        response_object['success']= True
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
        response_object['success']= True
        user_data=update_badges(user_data, challenges)
        user_data=update_stats(user_data, challenges)
        flag_modified(user_data, "stats")
        flag_modified(user_data, "badges")
        db.session.commit()
        user_data=UserData.query.get(user_id)
        #print("Stats", user_data.stats)
        #print("Badges", user_data.stats)
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
        response_object['success']= True
        return response_object


@app.route("/api/challenges", methods=["POST", "GET"])
@cross_origin()
def challenges_basic():
    response_object = {"status": "success"}
    if request.method == 'POST':
        data=request.get_json()
        user_id=data['userId']
        user_data=UserData.query.get(user_id) 
        c=random.choice(list(range(2, 10)))
        challenge_ids = [ c+x for x in range(3)] #add user personalization
        challenge_list = []
        for i in range(len(challenge_ids)):
            challenge = Challenges.query.get(challenge_ids[i])
            fact = Facts.query.filter_by(mode=challenge.mode).first()
            if user_data.favs!=None:
                favourite=True if challenge_ids[i] in user_data.favs else False
            else:
                favourite=False
            challenge_list.append(
                {
                    "id": challenge.id,
                    "title": challenge.task,
                    "droplets": challenge.droplets,
                    "fact": fact.fact,
                    "favourite": favourite,
                }
            )
        response_object['success']= True
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

@app.route("/api/challenge/all", methods=["POST", "GET"])
@cross_origin()
def challenges_all():
    response_object = {"status": "success"}
    if request.method == 'POST':
        data=request.get_json()
        user_id=data['userId']
        user_data=UserData.query.get(user_id)
        print(user_data.modes)
        if not(user_data.modes == []):
            challenges = Challenges.query.filter(Challenges.mode.in_(user_data.modes)).all()
        else:
            challenges = Challenges.query.all()[1:]
        #print(challenges)
        challenge_list=[]
        
        for c in challenges:
            fact = Facts.query.filter_by(mode=c.mode).first()
            if user_data.favs!=None:
                favourite=True if c.id in user_data.favs else False
            else:
                favourite=False
            challenge_list.append(
                {
                    "id": c.id,
                    "title": c.task,
                    "droplets": c.droplets,
                    "fact": fact.fact,
                    "favourite": favourite
                }
            )
        response_object['success']= True
        response_object["challenges"] =challenge_list
        return response_object

@app.route("/api/stats", methods=["POST", "GET"])
@cross_origin()
def stats():
    response_object = {"status": "success"}
    if request.method == 'POST':
        response_object['success']= True
        data=request.get_json()
        user_id=data['userId']
        user_data=UserData.query.get(user_id) 
        with open(str(os.path.dirname(os.path.abspath(__file__))) + "/data/graph1.png", "rb") as img:
            weekly = base64.b64encode(img.read()).decode('utf-8')
        with open(str(os.path.dirname(os.path.abspath(__file__))) + "/data/graph2.png", "rb") as img:
            monthly = base64.b64encode(img.read()).decode('utf-8')
        response_object['weekly']=weekly
        response_object['monthly']=monthly
        return response_object

@app.route("/api/friend/list", methods=["POST", "GET"])
@cross_origin()
def friends_list():
    response_object = {"status": "success"}
    if request.method == 'POST':
        response_object['success']= True
        data=request.get_json()
        user_id=data['userId']
        user_data=UserData.query.get(user_id)
        friends_list=[]
        for f in user_data.friends:
            friend=User.query.get(f)
            friend_data=UserData.query.get(f)
            challenge=Challenges.query.get(friend_data.challenge)
            friends_list.append(
                {
                    "FriendId":f,
                    "FriendName":friend.name,
                    "Challenge": "No challenge in progress" if challenge.task=="" else challenge.task
                }
            )
        response_object["friends"] = friends_list
        return response_object
        
@app.route("/api/friend/add", methods=["POST", "GET"])
@cross_origin()
def friends_add():
    response_object = {"status": "success"}
    if request.method == 'POST':
        response_object['success']= True
        data=request.get_json()
        user_id=data['userId']
        user=User.query.get(user_id)
        friend_name=data['friendName']
        if friend_name==user.name:
            response_object['success']= False
            return response_object
        friend=User.query.filter_by(name=friend_name).first()
        if friend is None:
            response_object['success']=False 
            return response_object
        user_data=UserData.query.get(user_id)
        friend_data=UserData.query.get(friend.id)
        if friend.id not in user_data.friends:
            user_data.friends.append(friend.id)
        challenge=Challenges.query.get(friend_data.challenge)
        response_object["FriendId"]=friend.id
        response_object["FriendName"]=friend.name
        response_object["Challenge"]= "No challenge in progress" if challenge.task=="" else challenge.task
        flag_modified(user_data,"friends")
        db.session.commit()
        print("Friends", UserData.query.get(user_id).friends)
        return response_object

@app.route("/api/favourite", methods=["POST", "GET"])
@cross_origin()
def favourite():
    response_object = {"status": "success"}
    if request.method == 'POST':
        response_object['success']= True
        data=request.get_json()
        user_id=data['userId']
        challenge_id=data['challengeId']
        fav=data['challengeId']
        user_data=UserData.query.get(user_id)
        if user_data.favs is None:
            user_data.favs=[]
        if fav:
            if challenge_id not in user_data.favs:
                user_data.favs.append(challenge_id)
        else:
            if challenge_id in user_data.favs:
                user_data.favs.remove(challenge_id)
        db.session.commit()
        return response_object

@app.route("/api/challenge/favs", methods=["POST", "GET"])
@cross_origin()
def favourites_list():
    response_object = {"status": "success"}
    if request.method == 'POST':
        response_object['success']= True
        data=request.get_json()
        user_id=data['userId']
        user_data=UserData.query.get(user_id)
        challenges = Challenges.query.filter(Challenges.id.in_(user_data.favs)).all()
        challenge_list=[]
        
        for c in challenges:
            fact = Facts.query.filter_by(mode=c.mode).first()
            challenge_list.append(
                {
                    "id": c.id,
                    "title": c.task,
                    "droplets": c.droplets,
                    "fact": fact.fact,
                    "favourite": True
                }
            )
        response_object["challenges"] =challenge_list
        return response_object
        
@app.route("/api/badges", methods=["POST", "GET"])
@cross_origin()
def badges():
    response_object = {"status": "success"}
    if request.method == 'POST':
        response_object['success']= True
        data=request.get_json()
        user_id=data['userId']
        user_data=UserData.query.get(user_id)
        badges=Badges.query.all()
        badges_list=[]
        for b in badges:
            badges_list.append(
                {
                    "BadgeId":b.id,
                    "BadgeName":b.badge,
                    "Possessed": True if b.id in user_data.badges else False
                }
            )
        response_object["badges"] =badges_list
        return response_object
        
        
@app.route('/api/friend', methods=['POST', 'GET'])
@cross_origin()
def friend_profile():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        response_object['success']= True
        data=request.get_json()
        user_id=data['UserId']
        friend_id=int(data['FriendId'])
        friend=User.query.get(friend_id)
        friend_data=UserData.query.get(friend_id)
        response_object['FriendId']=friend_id
        response_object['FriendName']=friend.name
        response_object['Droplets']=friend_data.droplets
        response_object['Streak']=friend_data.streak
        badges = Badges.query.filter(Badges.id.in_(friend_data.badges)).all()
        badges_list=[]
        for b in badges:
            badges_list.append(
                {
                    "BadgeId":b.id,
                    "BadgeName":b.badge,
                    "Possessed": True if b.id in friend_data.badges else False
                }
            )
        response_object["Badges"] =badges_list
        return response_object






