from flask import Flask, redirect, url_for
from flask_jwt_extended import JWTManager
from datetime import timedelta
from .home import home
from .auth import auth
from .profile import profile

app = Flask(__name__)
#TODO: Add secret key from config
app.secret_key = "00a617553ffe9f0a9aa84787683ab92cf1b152049b96f7ad0b160d9167fd04be"
#TODO: Add other configs
#TODO: Add logging

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True

jwt_manager = JWTManager(app)

@jwt_manager.unauthorized_loader
def unauthorized_callback(callback):
    return redirect(url_for('auth.login'), 302)

#TODO: Handle expired tokens
#TODO: Handle token refreshing automatically

app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(profile)