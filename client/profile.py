# this calendar contains read, create, delete
from flask import Blueprint, request, render_template, jsonify
from flask_jwt_extended import jwt_required

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

@profile.route('/data', methods=['GET'])
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    # use these variables to limit data 
    # events.json file used for demo purposes

    with open("events.json", "r") as input_data:
        # connect to backend and database
        # check out jsonfiy method or the built in json module
         return input_data.read()

@profile.route('/add_event', methods=['POST'])
def create_event():
    event_data = request.get_json()

    # TODO: Validate event_data

    with open('events.json', 'a') as f:
        f.write(json.dumps(event_data))

    return jsonify({'success': True}), 200

