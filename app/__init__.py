from flask import Flask
from .home import home
from .profile import profile

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(profile)