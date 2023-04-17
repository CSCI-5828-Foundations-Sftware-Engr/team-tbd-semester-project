import os
import logging
from configparser import ConfigParser
from datetime import datetime

from flask import Flask, request, Blueprint, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

import db


config = ConfigParser()
config.read('app_config.ini')

logger = logging.getLogger("Server log")
logger.setLevel(config['LOGGING']['level'])

# configure flask app
app = Flask(__name__, instance_relative_config=True)
app.secret_key = config['SERVER_INFO']['secret_key']
app.config['JSON_SORT_KEYS'] = False
api = Blueprint('api', __name__, url_prefix='/api')

# configure Flask-JWT
jwt_manager = JWTManager(app)


@jwt_manager.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    result = db.execute_query(f'SELECT token FROM revoked_tokens WHERE token = "{jti}";')
    result = result.fetchone()
    return result is not None


@api.route('/health')
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

    result = db.execute_query(f'SELECT password FROM users WHERE email = "{email}";')
    result = result.fetchone()

    if not result:
        return 'Invalid email or password.', 401

    pass_hash = result[0]

    if not check_password_hash(pass_hash, password):
        return 'Invalid email or password.', 401

    access_token = create_access_token(email)
    return jsonify({"access_token": access_token}), 200


@api.route('/logout', methods=['DELETE', 'POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.execute_insert(f'INSERT INTO revoked_tokens(token, created_timestamp) VALUES("{jti}", {datetime.now().timestamp()});')
    return "You have been logged out", 200


@api.route('/protected')
@jwt_required()
def protected():
    identity = get_jwt_identity()
    return f'You are authenticated {identity}', 200


app.register_blueprint(api)
app.run(host=config['SERVER_INFO']['host'], port=int(config['SERVER_INFO']['port']))
