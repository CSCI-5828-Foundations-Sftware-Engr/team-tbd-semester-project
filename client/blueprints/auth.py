import re
from flask import Blueprint, request, redirect, url_for, render_template, make_response, flash
import requests
from flask_jwt_extended import set_access_cookies, unset_access_cookies

auth_bp = Blueprint('auth', __name__, template_folder='templates')
password_regex = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'

# TODO: Remove this below function once meaningful protected APIs are designed later on
@auth_bp.route('/protected', methods=['GET'])
def protected():
    response = requests.get('http://127.0.0.1:5001/api/protected', cookies=request.cookies)
    if response.status_code == 200:
        return response.text, 200
    else:
        return 'Error: Unauthorized access', 401


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        if not email:
            error = 'Please enter an email.'
        elif not password:
            error = 'Please enter a password.'
        elif not confirm_password:
            error = 'Please confirm the password.'
        elif not password == confirm_password:
            request.form.password = ''
            request.form.confirmPassword = ''
            error = 'Passwords do not match. Please try again.'
        elif not (re.match(password_regex, password) and re.match(password_regex, confirm_password)):
            request.form.password = ''
            request.form.confirmPassword = ''
            error = 'Weak password! Ensure that the password is at least 8 characters long, with uppercase, lowercase, number, special characters.'
        else:
            server_response = requests.post('http://127.0.0.1:5001/api/signup', data=request.form)
            if server_response.ok:
                flash('You were successfully registered. Please log in.')
                return redirect(url_for('auth.login'))
            else:
                request.form.email = ''
                request.form.password = ''
                request.form.confirmPassword = ''
                error = 'Email is already registered.'
    return render_template('auth/signup.html', error=error)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email:
            error = 'Please enter an email.'
        elif not password:
            error = 'Please enter a password.'
        else:
            server_response = requests.post('http://127.0.0.1:5001/api/login', data=request.form)
            if server_response.ok:
                client_response = make_response(redirect(url_for('profile.calendar')))
                server_response_json = server_response.json()
                token = server_response_json['access_token']
                set_access_cookies(client_response, token)
                return client_response
            else:
                request.form.email = ''
                request.form.password = ''
                error = 'Invalid email or password.'

    return render_template('auth/login.html', error=error)


@auth_bp.route('/logout')
def logout():
    requests.delete('http://127.0.0.1:5001/api/logout', cookies=request.cookies)
    flash('Logged out successfully.')
    client_response = redirect(url_for('auth.login'))
    unset_access_cookies(client_response)
    return client_response
