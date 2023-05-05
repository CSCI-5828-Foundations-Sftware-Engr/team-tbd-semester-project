import os
from flask import Flask
from configparser import ConfigParser
from flask_jwt_extended import JWTManager

import home
import auth
import profile
import cache

# Reading Flask app configs from app_config.ini file
directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = directory + os.sep + 'app_config.ini'
config = ConfigParser()
config.read(config_file)

# Creating new Flask app 
app = Flask(__name__)
app.secret_key = config['APP_INFO']['secret_key']
app.config['JSON_SORT_KEYS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_CSRF_CHECK_FORM'] = True

# Registering client-side API blueprints
app.register_blueprint(auth.auth)
app.register_blueprint(home.home)
app.register_blueprint(profile.profile)

# Configuring JWTManager for flask app
jwt_manager = JWTManager(app)

# Configuring caching for flask app
cache.cache.init_app(app)

app.run(host=config['CLIENT_INFO']['host'], port=int(config['CLIENT_INFO']['port']))
