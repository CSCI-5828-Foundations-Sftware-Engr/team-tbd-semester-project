from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

import db

bp = Blueprint('matches', __name__)


def get_user_matches(user_id):
    query = f'SELECT c.name, m.start_date_time, m.home_team, m.away_team FROM matches m ' \
            f'JOIN known_scheduled_matches AS ksm  ON m.id = ksm.id ' \
            f'JOIN competitions c ON m.competiton = c.code '
    results = db.execute_query(query).fetchall()

    if results is None:
        return list()

    matches = [{
        'competition': result[0],
        'start_date_time': result[1],
        'home_team': result[2],
        'away_team': result[3],
        'title': f'{result[2]} vs {result[3]}',
        'start': result[1],
    } for result in results]
    return matches


@bp.route('/competitions', methods=['GET'])
def competitions():
    comps = db.execute_query(f"SELECT code, name FROM competitions;").fetchall()
    return dict(comps), 200


@bp.route('/preferences', methods=['GET'])
@jwt_required()
def get_preferred_competitions():
    result = db.execute_query(f"SELECT competition_code FROM user_preferred_competitions WHERE "
                              f"user_id = {get_jwt_identity()};").fetchall()

    if result is None:
        return list(), 200

    return list(code[0] for code in result), 200


@bp.route('/preferences', methods=['POST'])
@jwt_required()
def add_preferred_competitions():
    comps = list(request.form['competitions'])

    for comp in comps:
        db.execute_commit(f"INSERT INTO user_preferred_competitions(userid, competition_code) "
                          f"VALUES({get_jwt_identity()}, '{comp}');")
    return comps, 200


@bp.route('/preferences', methods=['DELETE'])
@jwt_required()
def delete_preferred_competitions():
    comps = tuple(request.form['competitions'])

    db.execute_commit(f"DELETE FROM user_preferred_competitions WHERE user_id = {get_jwt_identity()} AND "
                      f"competition_code in {comps};")
    
    return comps, 200


@bp.route('/matches', methods=['GET'])
@jwt_required()
def matches():
    return jsonify(get_user_matches(get_jwt_identity())), 200
