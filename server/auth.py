import logging
from flask import Blueprint, request, session, redirect, url_for
import flask_login


bp = Blueprint("auth", __name__, url_prefix='auth')
logger = None
login_manager = None


def initialize_auth(app_logger: logging.Logger, manager: flask_login.LoginManager):
    global logger, login_manager
    logger = app_logger
    login_manager = manager


@bp.route('/signup', methods=['POST'])
def signup():
    return 404


@bp.route('/login', methods=['POST'])
def login():
    session['userid'] = request.form['userid']
    return 'You have successfully logged in'


@bp.route('/logout', methods=['POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('userid', None)
    return 'You are logged out', 200
