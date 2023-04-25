import os
from configparser import ConfigParser
from flask import Flask

from flask_jwt_extended import JWTManager

import home
import auth
import profile


directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = directory + os.sep + 'app_config.ini'

config = ConfigParser()
config.read(config_file)

app = Flask(__name__)
app.secret_key = config['APP_INFO']['secret_key']

app.register_blueprint(home.home)
app.register_blueprint(auth.auth)
app.register_blueprint(profile.profile)

jwt_manager = JWTManager(app)

app.config['JSON_SORT_KEYS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_CSRF_CHECK_FORM'] = True

app.run(host=config['CLIENT_INFO']['host'], port=int(config['CLIENT_INFO']['port']))