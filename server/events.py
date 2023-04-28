# different version of the reminders.py file
import logging
from configparser import ConfigParser
from datetime import datetime
from flask import Flask, request, Blueprint, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
import json

import db

bp = Blueprint('reminders', __name__, url_prefix='/reminders')


@bp.route('/get_reminders')
# @jwt_required()
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    # id = get_jwt_identity()
    id = 1
    with open("events.json", "r") as input_data:
        events = json.load(input_data)
    return jsonify(events), 200


@bp.route('/add_event', methods=['POST'])
#@jwt_required()
def add_event():
    # id = get_jwt_identity()
    id = 1
    title = request.form['title']
    start_date = request.form['start_date']
    start_time = request.form['start_time']
    end_date = request.form['end_date']
    end_time = request.form['end_time']
    
    
    # Update events.json file with new event
    with open("events.json", "r+") as input_data:
        events = json.load(input_data)
        new_event = {
            "reminder_id": len(events)+1,
            "title": title,
            "start_date": start_date,
            "end_date": end_date,
            "start_time": start_time,
            "end_time": end_time,
            "repeat_id": "NULL"
        }
        events.append(new_event)
        input_data.seek(0)
        json.dump(events, input_data, indent=4)
        input_data.truncate()
    
    return "Event successfully added.", 200


@bp.route('/delete_event', methods=['POST', 'DELETE'])
# @jwt_required()
def delete_event():
    # id = get_jwt_identity()
    id = 1
    reminder_id = int(request.form['reminder_id'])
    
    # Update events.json file by removing the deleted event
    with open("events.json", "r+") as input_data:
        events = json.load(input_data)
        updated_events = [event for event in events if event['reminder_id'] != reminder_id]
        input_data.seek(0)
        json.dump(updated_events, input_data, indent=4)
        input_data.truncate()

    return "Event successfully deleted.", 200
