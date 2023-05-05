from flask import Blueprint, render_template, redirect, url_for

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def empty():
    return redirect(url_for('auth.login'))

@home.route('/home')
def index():
    return render_template('home/home.html')

@home.route('/about')
def about():
    # TODO: Update about.html with latest README.md/wiki content
    return render_template('home/about.html')

@home.route('/contactUs')
def contactUs():
    return render_template('home/contactUs.html')