from flask import Flask
from client.client import client

app = Flask(__name__)

app.register_blueprint(client)