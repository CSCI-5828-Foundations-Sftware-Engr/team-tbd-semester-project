from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='/templates/home')

@home.route("/")
@home.route('/home')
def index():
    return render_template('login.html')

@home.route('/about')
def about():
    return render_template('about.html')

@home.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')