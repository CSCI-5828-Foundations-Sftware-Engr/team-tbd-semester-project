from flask import Blueprint, request, redirect, url_for, render_template, make_response, flash
from flask_jwt_extended import set_access_cookies, unset_access_cookies
import requests
import re

auth = Blueprint('auth', __name__, template_folder="templates")
passwordRegex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

# TODO: Remove this below function once meaningful protected apis are designed later on
@auth.route('/protected', methods=['GET'])
def protected():
    response = requests.get('http://127.0.0.1:5001/api/protected', cookies=request.cookies)
    if response.status_code == 200:
        return response.text, 200
    else:
        return 'Error: Unauthorized access', 401

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']

        if not email:
            error = 'Please enter an email.'
        elif not password:
            error = 'Please enter a password.'
        elif not confirmPassword:
            error = 'Please confirm the password.'
        elif not password == confirmPassword:
            request.form.password = ""
            request.form.confirmPassword = ""
            error = 'Passwords do not match. Please try again.'
        elif not (re.match(passwordRegex, password) and re.match(passwordRegex, confirmPassword)):
            request.form.password = ""
            request.form.confirmPassword = ""
            error = 'Weak password! Ensure that the password is at least 8 characters long, with uppercase, lowercase, number, special characters.'
        else:
            serverResponse = requests.post('http://127.0.0.1:5001/api/signup', data=request.form)
            if serverResponse.ok:
                flash("You were successfully registered. Please log in.")
                return redirect(url_for('auth.login'))
            else:
                request.form.email = ""
                request.form.password = ""
                request.form.confirmPassword = ""
                error = "Email is already registered."
    return render_template('home/signup.html', error=error)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not (request.form and request.form['email']):
            error = 'Please enter an email.'
        elif not (request.form and request.form['password']):
            error = 'Please enter a password.'
        else:
            serverResponse = requests.post('http://127.0.0.1:5001/api/login', data=request.form)
            if serverResponse.ok:
                clientResponse = make_response(redirect(url_for('profile.calendar')))
                serverResponseJSON = serverResponse.json()
                token = serverResponseJSON['access_token']
                set_access_cookies(clientResponse, token)
                return clientResponse
            else:
                request.form.email = ''
                request.form.password = ''
                error = "Invalid email or password."

    return render_template('home/login.html', error=error)

@auth.route('/logout')
def logout():
    requests.delete('http://127.0.0.1:5001/api/logout', cookies=request.cookies)
    flash('Logged out successfully.')
    clientResp = redirect(url_for('auth.login'))
    unset_access_cookies(clientResp)
    return clientResp
