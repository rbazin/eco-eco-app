from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)# CORS allowed for all domains on all routes

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000), unique=True)

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

@app.route("/login", methods=['POST', 'GET'])
@cross_origin()
def login():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data=request.get_json()
        print(data)
        """
        name = request.form.get('username')
        password = request.form.get('password')

        
        user = User.query.filter_by(name=name).first()

        if not user or not check_password_hash(user.password, password): 
            flash('Pease check your login details and try again.')
            return jsonify("NOT OK") # if user doesn't exist or password is wrong, reload the page
        

        else:
            login_user(user)
            return jsonify("OK")

        """
        return jsonify(response_object)

"""
@app.route("/home")
@login_required
def home():
    return 'you are in the home page'

@app.route('/signup', methods=['POST', 'GET'])
@cross_origin()
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(name=name).first() 

        if user: # if a user is found, we want to redirect back to signup page so user can try again  
            flash('User name already exists')
            return redirect(url_for('signup'))

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(name=name, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter_by(name=name).first()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/modes/<user_id>')
@login_required
def modes():
    modes={'car', 'bus'}
    return render_template('modes.html', data=modes)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
"""
