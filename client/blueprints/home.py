from flask import Blueprint, render_template, redirect, url_for

home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/')
def empty():
    return redirect(url_for('auth.login'))

@home_bp.route('/home')
def index():
    return render_template('home/home.html')

@home_bp.route('/about')
def about():
    # TODO: Update about.html with latest README.md/wiki content
    return render_template('home/about.html')

@home_bp.route('/contact-us')
def contact_us():
    return render_template('home/contactUs.html')
