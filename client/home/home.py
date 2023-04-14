from flask import Blueprint, render_template, request

home = Blueprint('home', __name__, template_folder='templates')

@home.route("/")
@home.route('/home')
def index():
    return render_template('home/home.html')

@home.route('/about')
def about():
    return render_template('home/about.html')

@home.route('/contactUs')
def contactUs():
    return render_template('home/contactUs.html')

@home.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        pass
    return render_template('home/signUp.html')

@home.route('/logIn', methods=['GET', 'POST'])
def logIn():
    error = None
    if request.method == 'POST':
        if request.form['email'] == 'admin@admin.com' and request.form['password'] == 'admin':
            pass
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('home/logIn.html', error=error)

@home.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    if request.method == 'POST':
        pass
    return render_template('home/forgotPassword.html')