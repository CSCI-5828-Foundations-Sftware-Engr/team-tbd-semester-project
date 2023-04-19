from flask import Blueprint, render_template

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