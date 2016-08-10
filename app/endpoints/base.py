from flask import Blueprint
from flask_jwt import jwt_required

base = Blueprint("base", __name__)


@base.route("/")
def index():
    return 'API index'


@base.route("/protected")
@jwt_required()
def protected():
    return "I am a protected route"
