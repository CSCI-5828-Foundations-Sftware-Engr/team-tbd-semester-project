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
app = Flask(__name__)
app.config['SECRET_KEY'] = config.get('APP_INFO', 'secret_key')
app.config['JSON_SORT_KEYS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_CSRF_IN_COOKIES'] = True

# Registering client-side API blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(profile_bp)

# Configuring JWTManager for Flask app
jwt = JWTManager(app)

# Configuring caching for Flask app
cache.init_app(app)

if __name__ == '__main__':
    host = config.get('CLIENT_INFO', 'host')
    port = config.getint('CLIENT_INFO', 'port')
    app.run(host=host, port=port)
