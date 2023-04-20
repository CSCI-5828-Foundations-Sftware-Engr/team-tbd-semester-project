from flask import Flask, redirect, url_for
from datetime import timedelta

from flask_jwt_extended import JWTManager

import home
import auth
import profile

app = Flask(__name__)
#TODO: Add secret key from config
app.secret_key = "secret"
#TODO: Add other configs
#TODO: Add logging


#TODO: Handle expired tokens
#TODO: Handle token refreshing automatically

app.register_blueprint(home.home)
app.register_blueprint(auth.auth)
app.register_blueprint(profile.profile)

jwt_manager = JWTManager(app)

app.config['JSON_SORT_KEYS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True
app.config['JWT_SECRET_KEY'] = 'jwtsecret'

app.run(host='127.0.0.1', port=5000, debug=True)
