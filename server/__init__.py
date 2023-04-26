import logging
from configparser import ConfigParser
from datetime import timedelta

from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager

import auth
import matches
import db
import reminders

directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = directory + os.sep + 'app_config.ini'

config = ConfigParser()
config.read(config_file)

logger = logging.getLogger("Server log")
logger.setLevel(config['LOGGING']['level'])

# configure flask app
app = Flask(__name__, instance_relative_config=True)
app.secret_key = config['APP_INFO']['secret_key']

# configure Flask-JWT
jwt_manager = JWTManager(app)
app.config['JSON_SORT_KEYS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_CSRF_CHECK_FORM'] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(int(config['SERVER_INFO']['token_expiry_time']))

api = Blueprint('api', __name__, url_prefix='/api')


@jwt_manager.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    result = db.execute_query(f'SELECT token FROM revoked_tokens WHERE token = "{jti}";')
    result = result.fetchone()
    return result is not None


@api.route('/health')
def health():
    return "Sever is up and running.", 200


api.register_blueprint(auth.bp)
api.register_blueprint(matches.bp)
api.register_blueprint(reminders.bp)
app.register_blueprint(api)
app.run(host=config['SERVER_INFO']['host'], port=int(config['SERVER_INFO']['port']))
