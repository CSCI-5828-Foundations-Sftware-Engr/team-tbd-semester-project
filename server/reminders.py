from datetime import datetime, timedelta
from flask import request, Blueprint, jsonify
from flask_jwt_extended import  jwt_required, get_jwt_identity

from matches import get_user_matches
import db

bp = Blueprint('reminders', __name__, url_prefix='/reminders')


def get_user_reminders(user_id):
    result = db.execute_query(f'SELECT * FROM reminders WHERE userid = "{user_id}";').fetchall()
    events = []
    for event in result:
        events.append(
            {"reminder_id": event[0], "title": event[2], "description": event[3], "start_time": event[4],
             "end_time": event[5], "reminder_type": event[6], "progress": event[7], "time_taken": event[8],
             "repeat_id": event[9]})
    return events


@bp.route('/get_reminders')
@jwt_required()
def return_data():
    return jsonify({"reminders": get_user_reminders(get_jwt_identity())}), 200


@bp.route('/add_event', methods=['POST'])
@jwt_required()
def add_event():
    user_id = get_jwt_identity()
    title = request.form['title']
    description = request.form['description']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    reminder_type = request.form['reminder_type']
    progress = request.form['progress']
    db.execute_commit(
        f'INSERT INTO reminders(userid, title, description, start_time_stamp, end_time_stamp, reminder_type, progress) '
        f'VALUES("{user_id}", "{title}", "{description}", "{start_time}", "{end_time}", "{reminder_type}", "{progress}");')
    return "Event successfully added.", 200


@bp.route('/delete_event', methods=['POST', 'DELETE'])
@jwt_required()
def delete_event():
    user_id = get_jwt_identity()
    if 'repeat_id' in request.form:
        repeat_id = request.form['repeat_id']
        db.execute_commit(f'DELETE FROM repeated_reminders WHERE id = "{repeat_id}" AND userid = "{user_id}";')
        return "Repeated event successfully deleted.", 200
    else:
        reminder_id = request.form['reminder_id']
        db.execute_commit(f'DELETE FROM reminders WHERE reminder_id = "{reminder_id}" AND userid = "{user_id}";')
        return "Event successfully deleted.", 200


@bp.route('/calendar', methods=['GET'])
@jwt_required()
def calendar():
    reminders = get_user_reminders(get_jwt_identity())
    matches = get_user_matches(get_jwt_identity())

    for match in matches:
        for reminder in reminders:

            date_format = "%Y-%m-%d %H:%M:%S"
            reminder_start_time = datetime.strptime(reminder['start_time'], date_format)
            match_start_time = datetime.strptime(match['start_date_time'], date_format)
            reminder_end_time = datetime.strptime(reminder['end_time'], date_format)
            match_end_time = match_start_time + timedelta(hours=2) #FIX

            if (match_start_time < reminder_start_time < match_end_time) or (
                    match_start_time < reminder_end_time < match_end_time):
                matches.remove(match)

    return jsonify({"reminders": reminders, 'matches': matches}), 200
