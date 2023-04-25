from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

import db

bp = Blueprint('matches', __name__)


@bp.route('/competitions', methods=['GET'])
def competitions():
    comps = db.execute_query(f"SELECT code, name FROM competitions;").fetchall()
    return dict(comps), 200


@bp.route('/preferences', methods=['GET'])
@jwt_required()
def get_preferred_competitions():
    result = list(db.execute_query(f"SELECT competition_code FROM user_preferred_competitions WHERE "
                                   f"user_id = {get_jwt()};").fetchall())

    if result is None:
        return list(), 200

    return list(code[0] for code in result), 200


@bp.route('/preferences', methods=['POST'])
@jwt_required()
def add_preferred_competitions():
    comps = list(request.form['competitions'])

    for comp in comps:
        db.execute_commit(f"INSERT INTO user_preferred_competitions(userid, competition_code) "
                          f"VALUES({get_jwt()}, '{comp}');")
    return comps, 200


@bp.route('/preferences', methods=['DELETE'])
@jwt_required()
def delete_preferred_competitions():
    comps = tuple(request.form['competitions'])

    db.execute_commit(f"DELETE FROM user_preferred_competitions WHERE user_id = {get_jwt()} AND "
                      f"competition_code in {comps};")
    
    return comps, 200
