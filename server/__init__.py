import os
from flask import Flask, Blueprint, request, session
import logging
from configparser import ConfigParser
from flask_login.login_manager import LoginManager

import auth


if __name__ == "__main__":
    path_current_directory = os.path.dirname(__file__)
    config_file = os.path.join(path_current_directory, 'app_config.ini')
    config = ConfigParser()
    config.read(config_file)

    logger = logging.getLogger("Server log")
    logger.setLevel(config['LOGGING']['level'])

    # configure flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config['JSON_SORT_KEYS'] = False
    app.secret_key = config['SERVER_INFO']['secret_key']
    login_manager = LoginManager(app)

    # all api calls will begin with /api...
    bp = Blueprint("api", __name__, url_prefix='/api')

    @app.route('/', methods=['GET'])
    def index():
        if 'userid' not in session:
            return 'You are not logged in', 400
        else:
            return 'You are logged in', 200


    @bp.route('/health')
    def health():
        return "Sever is up and running running", 200

    auth.initialize_auth(logger, login_manager)
    bp.register_blueprint(auth.bp)

    app.register_blueprint(bp)
    app.run(host=config['SERVER_INFO']['host'], port=int(config['SERVER_INFO']['port']))

