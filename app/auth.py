from flask import Blueprint, request, redirect, url_for, render_template, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt, set_access_cookies, unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db

auth = Blueprint('auth', __name__, template_folder="templates")

@auth.route('/protected')
@jwt_required()
def protected():
    identity = get_jwt_identity()
    return f'You are authenticated {identity}', 200

@auth.route('/signUp', methods=['GET', 'POST'])
def signUp():
    error = None
    if request.method == 'POST':
        if not (request.form and request.form['email']):
            error = 'Please enter an email.'
        elif not (request.form and request.form['password']):
            error = 'Please enter a password.'
        else:
            email = request.form['email']
            result = db.execute_query(f'SELECT userid FROM users WHERE email = "{email}";').fetchone()

            if result:
                error = "Email is already registered."
            else:
                password = generate_password_hash(request.form['password'])
                db.execute_insert(f'INSERT INTO users(email, password) VALUES("{email}", "{password}");')
                return redirect(url_for('auth.logIn'))
    return render_template('home/signUp.html', error=error)

@auth.route('/logIn', methods=['GET', 'POST'])
def logIn():
    error = None
    if request.method == 'POST':
        if not (request.form and request.form['email']):
            error = 'Please enter an email.'
        elif not (request.form and request.form['password']):
            error = 'Please enter a password.'
        else:
            email = request.form['email']
            result = db.execute_query(f'SELECT password FROM users WHERE email = "{email}";').fetchone()

            if not result:
                error = 'Invalid email or password.'
            else:
                password = request.form['password']
                pass_hash = result[0]

                if not check_password_hash(pass_hash, password):
                    error = 'Invalid email or password. 2'
                else:
                    #TODO: Handle tokens; Global?
                    access_token = create_access_token(email)
                    #TODO: Add calendar.html path below
                    resp = make_response(redirect(url_for('home.index')))
                    set_access_cookies(resp, access_token)
                    return resp

    return render_template('home/logIn.html', error=error)

@auth.route('/logout')
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.execute_insert(f'INSERT INTO revoked_tokens(token, created_timestamp) VALUES("{jti}", {datetime.now().timestamp()});')
    resp = make_response("You have been logged out", 200)
    unset_jwt_cookies(resp)
    return resp

@auth.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    if request.method == 'POST':
        pass
    return render_template('home/forgotPassword.html')