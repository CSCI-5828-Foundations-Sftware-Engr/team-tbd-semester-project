from flask import Blueprint, request, render_template
from flask_jwt_extended import jwt_required
import requests
import json
from datetime import datetime

profile_bp = Blueprint('profile', __name__, template_folder='templates')

@profile_bp.route('/calendar')
def calendar():
    return render_template("profile/calendar.html")

@profile_bp.route('/calendarUserData')
def return_data():
    try:
        url = f'http://127.0.0.1:5001/api/reminders/calendar'
        response = requests.get(url, cookies=request.cookies)
        data = response.json()
        reminders = data.get('reminders', [])
        return json.dumps(reminders)
    except Exception as e:
        return f'Error getting data: {e}', 500

@profile_bp.route('/calendarMatchesData')
def return_data_matches():
    try:
        url = f'http://127.0.0.1:5001/api/reminders/calendar'
        response = requests.get(url, cookies=request.cookies)
        data = response.json()
        matches = data.get('matches', [])
        return json.dumps(matches)
    except Exception as e:
        return f'Error getting data: {e}', 500

@profile_bp.route('/add_event', methods=['POST'])
def add_event():
    data = {
        'title': request.form['title'],
        'start_time': datetime.strptime(request.form['start_date'] + ' ' +request.form['start_time'], '%Y-%m-%d %H:%M'),
        'end_time': datetime.strptime(request.form['end_date'] + ' ' +request.form['end_time'], '%Y-%m-%d %H:%M'),
    }
    response = requests.post('http://127.0.0.1:5001/api/reminders/add_event', data=data, cookies=request.cookies)
    return '' 

@profile_bp.route('/delete_event', methods=['POST'])
def delete_event():
    response = requests.post('http://127.0.0.1:5001/api/reminders/delete_event', data=request.form, cookies=request.cookies)
    return 'Successfully deleted event'
