import logging
from configparser import ConfigParser
from datetime import datetime
from flask import Flask, request, Blueprint, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
import db

bp = Blueprint('reminders', __name__, url_prefix='/reminders')


@bp.route('/get_reminders')
# @jwt_required()
def return_data():
    # id = get_jwt_identity()
    id = 1
    result = db.execute_query(f'SELECT * FROM reminders WHERE userid = "{id}";')
    events = []
    for event in result:
        events.append(
            {"reminder_id": event[0], "title": event[2], "description": event[3], "start_time": event[4],
             "end_time": event[5], "reminder_type": event[6], "progress": event[7], "time_taken": event[8],
             "repeat_id": event[9]})
    return jsonify(events), 200


@bp.route('/add_event', methods=['POST'])
#@jwt_required()
def add_event():
    # id = get_jwt_identity()
    id = 1
    title = request.form['title']
    description = request.form['description']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    reminder_type = request.form['reminder_type']
    progress = request.form['progress']
    db.execute_insert(
        f'INSERT INTO reminders(userid, title, description, start_time_stamp, end_time_stamp, reminder_type, progress) VALUES("{id}", "{title}", "{description}", "{start_time}", "{end_time}", "{reminder_type}", "{progress}");')
    return "Event successfully added.", 200


@bp.route('/delete_event', methods=['POST', 'DELETE'])
# @jwt_required()
def delete_event():
    # id = get_jwt_identity()
    id = 1
    repeat_id = request.form['repeat_id']
    reminder_id = request.form['reminder_id']
    if repeat_id != "NULL":
        db.execute_insert(f'DELETE FROM repeated_reminders WHERE id = "{repeat_id}" AND userid = "{id}";')
        return "Repeated event successfully deleted.", 200
    else:
        db.execute_insert(f'DELETE FROM reminders WHERE reminder_id = "{reminder_id}" AND userid = "{id}";')
        return "Event successfully deleted.", 200