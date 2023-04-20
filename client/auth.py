from flask import Blueprint, request, redirect, url_for, render_template, make_response, flash
from flask_jwt_extended import set_access_cookies, decode_token
from werkzeug.security import generate_password_hash, check_password_hash
import requests

auth = Blueprint('auth', __name__, template_folder="templates")


# TODO: Remove this below function once meaningful protected apis are designed later on
@auth.route('/protected', methods=['GET'])
def protected():
    response = requests.get('http://127.0.0.1:5001/api/protected', cookies=request.cookies)
    if response.status_code == 200:
        return response.text
    else:
        return 'Error: Unauthorized access'


@auth.route('/signUp', methods=['GET', 'POST'])
def signUp():
    error = None
    if request.method == 'POST':
        if not (request.form and request.form['email']):
            error = 'Please enter an email.'
        elif not (request.form and request.form['password']):
            error = 'Please enter a password.'
        else:
            response = requests.post('http://127.0.0.1:5001/api/signUp', data=request.form)
            if response.ok:
                #TODO: Add flash message indicating successful signup
                flash("You were successfully registered. Please log in.", "success")
                return redirect(url_for('auth.login'))
            else:
                request.form.email = ""
                request.form.password = ""
                error = "Email is already registered."
    return render_template('home/signUp.html', error=error)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not (request.form and request.form['email']):
            error = 'Please enter an email.'
        elif not (request.form and request.form['password']):
            error = 'Please enter a password.'
        else:
            response = requests.post('http://127.0.0.1:5001/api/login', data=request.form)

            if response.ok:
                #TODO: Redirect to calendar view on successful login
                resp = make_response(redirect(url_for('profile.calendar')))
                json_resp = response.json()
                token = json_resp['access_token']
                set_access_cookies(resp, token)
                return resp
            else:
                request.form.email = ''
                request.form.password = ''
                error = "Invalid email or password."

    return render_template('home/login.html', error=error)

@auth.route('/logout')
def logout():
    #TODO: Determine whether to add back the revoked-token code from earlier
    resp = make_response("You have been logged out", 200)
    return resp

@auth.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    #TODO: Handle error
    #TODO: Handle forgotPassword POST call
    if request.method == 'POST':
        pass
    return render_template('home/forgotPassword.html')