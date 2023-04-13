from flask import Flask
from flask import request, render_template, jsonify
import json


app = Flask(__name__)


@app.route('/calendar')
def calendar():
    return render_template("calendar.html")


@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    # use these variables to limit data 
    # text file used for demo purposes

    with open("events.json", "r") as input_data:
        # connect to backend and backend to database
        # check out jsonfiy method or the built in json module

        return input_data.read()

if __name__ == '__main__':
    app.debug = True
    app.run()
