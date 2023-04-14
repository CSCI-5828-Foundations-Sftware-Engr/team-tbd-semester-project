from flask import Blueprint
from client.home.home import home
from client.profile.profile import profile

client = Blueprint('client', __name__,)

client.register_blueprint(home)
client.register_blueprint(profile)