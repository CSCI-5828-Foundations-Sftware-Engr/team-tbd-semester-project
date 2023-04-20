from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

import db

bp = Blueprint('auth', __name__)


# TODO: Remove this below function once meaningful protected apis are designed later on
@bp.route('/protected')
@jwt_required()
def protected():
    identity = get_jwt_identity()
    email = db.execute_query(f"SELECT email FROM users WHERE userid = {identity};").fetchone()[0]

    return f'You are authenticated {email}', 200


@bp.route('/signUp', methods=['GET', 'POST'])
def signUp():
    email = request.form['email']
    password = generate_password_hash(request.form['password'])

    result = db.execute_query(f'SELECT userid FROM users WHERE email = "{email}";')
    result = result.fetchone()

    if result:
        return "Email is already registered.", 401

    db.execute_insert(f'INSERT INTO users(email, password) VALUES("{email}", "{password}");')
    return "User registered.", 200


@bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    result = db.execute_query(f'SELECT userid, password FROM users WHERE email = "{email}";').fetchone()

    if not result:
        return make_response("Invalid email or password.", 401)
    
    userid = result[0]
    pass_hash = result[1]

    if not check_password_hash(pass_hash, password):
        return make_response("Invalid email or password.", 401)
    else:
        access_token = create_access_token(userid)
        resp = make_response({"access_token": access_token}, 200)
        return resp


@bp.route('/logout', methods=['POST', 'DELETE'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.execute_insert(f"INSERT INTO revoked_tokens(token, timestamp) VALUES('{jti}', "
                      f"{datetime.timestamp(datetime.now(tz=timezone.utc))})")
    resp = make_response("You have been logged out", 200)
    return resp


@bp.route('/forgotPassword', methods=['POST'])
def forgotPassword():
    #TODO: Handle error
    #TODO: Handle forgotPassword POST call
    if request.method == 'POST':
        pass
