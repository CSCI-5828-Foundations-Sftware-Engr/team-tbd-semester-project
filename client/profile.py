from flask import Blueprint, request, render_template
from flask_jwt_extended import jwt_required
import requests
import jsonpickle

profile = Blueprint('profile', __name__, template_folder='templates')

# @profile.route('/')
# @jwt_required()
# def index():
#     return ''

@profile.route('/')
@profile.route('/profile')
def index():
    return render_template("profile/profile.html")

@profile.route('/calendar')
def calendar():
    return render_template("profile/calendar.html")

@profile.route('/tasks')
def tasks():
    return render_template("profile/tasks.html")

@profile.route('/progress')
def progress():
    return render_template("profile/progress.html")

@profile.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    # use these variables to limit data 
    # events.json file used for demo purposes

    response = requests.get('http://127.0.0.1:5001/api/reminders/calendar', cookies=request.cookies)
    matches, reminders = response.json()['matches'], response.json()['reminders']
    return jsonpickle.encode(reminders)

@profile.route('/datamatches')
def return_data_matches():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    # use these variables to limit data 
    # events.json file used for demo purposes

    response = requests.get('http://127.0.0.1:5001/api/reminders/calendar', cookies=request.cookies)
    matches, reminders = response.json()['matches'], response.json()['reminders']
    return jsonpickle.encode(matches)
