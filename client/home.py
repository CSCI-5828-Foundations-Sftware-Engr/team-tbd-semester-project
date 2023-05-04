from flask import Blueprint, render_template
import os

home = Blueprint('home', __name__)

@home.route("/")
@home.route('/home')
def index():
    return render_template('home/login.html')

@home.route('/about')
def about():
    return render_template('home/about.html')

@home.route('/contactUs')
def contactUs():
    return render_template('home/contactUs.html')