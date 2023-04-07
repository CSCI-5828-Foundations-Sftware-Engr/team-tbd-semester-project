import os
from flask import Flask, Blueprint, request
import logging
from configparser import ConfigParser
from flask_login.login_manager import LoginManager
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import User
import db


path_current_directory = os.path.dirname(__file__)
config_file = os.path.join(path_current_directory, 'app_config.ini')
config = ConfigParser()
config.read(config_file)

logger = logging.getLogger("Server log")
logger.setLevel(config['LOGGING']['level'])

# configure flask app
app = Flask(__name__, instance_relative_config=True)
app.config['JSON_SORT_KEYS'] = False
app.secret_key = config['SERVER_INFO']['secret_key']

login_manager = LoginManager(app)

api = Blueprint("api", __name__, url_prefix='/api')


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return "Unauthorized", 401


@api.route('/health')
@login_required
def health():
    return "Sever is up and running.", 200


@api.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = generate_password_hash(request.form['password'])

    result = db.execute_query(f'SELECT userid FROM users WHERE email = "{email}";')
    result = result.fetchone()

    if result:
        return "Email is already registered.", 401

    db.execute_insert(f'INSERT INTO users(email, password) VALUES("{email}", "{password}");')
    return "User registered.", 200


@api.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    result = db.execute_query(f'SELECT userid, password FROM users WHERE email = "{email}";')
    result = result.fetchone()

    if not result:
        return "Invalid email or password.", 401

    userid = result[0]
    pass_hash = result[1]

    if not check_password_hash(pass_hash, password):
        return "Invalid email or password.", 401

    login_user(User(userid))
    return "You are logged in.", 200


@api.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return "You have been logged out", 200


app.register_blueprint(api)
app.run(host=config['SERVER_INFO']['host'], port=int(config['SERVER_INFO']['port']))
