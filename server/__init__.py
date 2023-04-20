import logging
from configparser import ConfigParser
from datetime import timedelta

from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager

import auth


config = ConfigParser()
config.read('app_config.ini')

logger = logging.getLogger("Server log")
logger.setLevel(config['LOGGING']['level'])

# configure flask app
app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'secret'

# configure Flask-JWT
jwt_manager = JWTManager(app)
app.config['JSON_SORT_KEYS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True
app.config['JWT_SECRET_KEY'] = 'jwtsecret'

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/health')
def health():
    return "Sever is up and running.", 200


api.register_blueprint(auth.bp)
app.register_blueprint(api)
app.run(host=config['SERVER_INFO']['host'], port=int(config['SERVER_INFO']['port']))