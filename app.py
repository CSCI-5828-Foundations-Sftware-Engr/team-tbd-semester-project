from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/logIn', methods=['GET', 'POST'])
def logIn():
    error = None
    if request.method == 'POST':
        if request.form['email'] == 'admin@admin.com' and request.form['password'] == 'admin':
            pass
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('logIn.html', error=error)

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        pass
    return render_template('signUp.html')

@app.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    if request.method == 'POST':
        pass
    return render_template('forgotPassword.html')

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')