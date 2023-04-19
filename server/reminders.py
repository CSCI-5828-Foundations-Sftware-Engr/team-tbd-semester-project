import logging
from configparser import ConfigParser
from datetime import datetime

from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity




bp = Blueprint("reminders", __name__)


@bp.route("/reminders", methods=["GET"])
@jwt_required()
def get_reminders():
    userid = get_jwt_identity()


