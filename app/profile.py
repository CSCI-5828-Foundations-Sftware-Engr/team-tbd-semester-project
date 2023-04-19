from flask import Blueprint
from flask_jwt_extended import jwt_required

profile = Blueprint('profile', __name__, template_folder='templates')

@profile.route('/')
@jwt_required()
def index():
    return ''