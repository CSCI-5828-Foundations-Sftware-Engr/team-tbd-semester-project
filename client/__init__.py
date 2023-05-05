import os
from configparser import ConfigParser

from flask import Flask
from flask_jwt_extended import JWTManager

from blueprints.auth import auth_bp
from blueprints.home import home_bp
from blueprints.profile import profile_bp
from cache import cache

# Reading Flask app configs from app_config.ini file
directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(directory, 'app_config.ini')
config = ConfigParser()
config.read(config_file)

# Creating new Flask app 
client_app = Flask(__name__)
client_app.config['SECRET_KEY'] = config.get('APP_INFO', 'secret_key')
client_app.config['JSON_SORT_KEYS'] = False
client_app.config['JWT_TOKEN_LOCATION'] = ['cookies']
client_app.config['JWT_COOKIE_CSRF_PROTECT'] = False
client_app.config['JWT_CSRF_IN_COOKIES'] = True

# Registering client-side API blueprints
client_app.register_blueprint(auth_bp)
client_app.register_blueprint(home_bp)
client_app.register_blueprint(profile_bp)

# Configuring JWTManager for Flask app
jwt = JWTManager(client_app)

# Configuring caching for Flask app
cache.init_app(client_app)

if __name__ == '__main__':
    host = config.get('CLIENT_INFO', 'host')
    port = config.getint('CLIENT_INFO', 'port')
    #client_app.run(host=host, port=port)
