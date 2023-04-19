from flask import Blueprint, request, redirect, url_for, render_template, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, set_access_cookies, unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
import requests

auth = Blueprint('auth', __name__, template_folder="templates")

#TODO: Remove this below function once meaningful protected apis are designed later on
@auth.route('/protected')
@jwt_required()
def protected():
    response = requests.get('http://127.0.0.1:5001/api/protected', cookies=request.cookies, headers=request.headers)
    if response.status_code == 200:
        return response.text
    else:
        return 'Error: Unauthorized access'

@auth.route('/signUp', methods=['GET', 'POST'])
def signUp():
     pass
#     error = None
#     if request.method == 'POST':
#         if not (request.form and request.form['email']):
#             error = 'Please enter an email.'
#         elif not (request.form and request.form['password']):
#             error = 'Please enter a password.'
#         else:
#             email = request.form['email']
#             result = db.execute_query(f'SELECT userid FROM users WHERE email = "{email}";').fetchone()
#
#             if result:
#                 error = "Email is already registered."
#             else:
#                 password = generate_password_hash(request.form['password'])
#                 db.execute_insert(f'INSERT INTO users(email, password) VALUES("{email}", "{password}");')
#                 #TODO: Add flash message indicating successful signup
#                 return redirect(url_for('auth.login'))
     #return render_template('home/signUp.html', error=error)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not (request.form and request.form['email']):
            error = 'Please enter an email.'
        elif not (request.form and request.form['password']):
            error = 'Please enter a password.'
        else:
            response = requests.post('http://127.0.0.1:5001/api/login', data=request.form, cookies=request.cookies)

            if response.ok:
                access_token = create_access_token(request.form['email'])
                resp = make_response(redirect(url_for('home.index')), 200)
                set_access_cookies(resp, access_token)
                return resp
            else:
                error = response.reason

    return render_template('home/login.html', error=error)

@auth.route('/logout')
@jwt_required()
def logout():
    #TODO: Determine whether to add back the revoked-token code from earlier
    resp = make_response("You have been logged out", 200)
    unset_jwt_cookies(resp)
    return resp

@auth.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    #TODO: Handle error
    #TODO: Handle forgotPassword POST call
    if request.method == 'POST':
        pass
    return render_template('home/forgotPassword.html')