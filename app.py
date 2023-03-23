from flask import Flask, render_template, request

app = Flask(__name__)

plans = [{"plan_title": "HW5 Submission", "plan_description": '"The work above is due by Thursday, March 22 2023 at 11:59pm. By that time, you should have completed the tasks above. We will review your user stories and confirm that we can access the simple web form you created for task 5."'}]

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        temp = {}
        for key, value in request.form.items():
            print(key, value)
            temp[key] = value
        plans.append(temp)
        print(plans)
    return render_template('index.html', plans=plans)
