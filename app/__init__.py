from flask import Flask, request

from .services import USER_SERVICE
from .utils import forward_request_to_service

app = Flask(__name__)


@app.route("/")
def index():
    return 'API index'


@app.route("/user")
def user_index():
    return forward_request_to_service(request, USER_SERVICE, "")
