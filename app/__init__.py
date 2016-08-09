import datetime

from flask import Flask, current_app, jsonify, request

from flask_jwt import JWT

from .exceptions import CustomError
from .services import USER_SERVICE
from .settings import SECRET_KEY
from .utils import authenticate, forward_request_to_service, identity

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

jwt = JWT(app, authenticate, identity)


@jwt.jwt_payload_handler
def payload_handler(identity):
    print(identity)
    iat = datetime.datetime.utcnow()
    exp = iat + current_app.config.get('JWT_EXPIRATION_DELTA')
    nbf = iat + current_app.config.get('JWT_NOT_BEFORE_DELTA')
    identity = identity['id']
    return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': identity}


@app.errorhandler(CustomError)
def custom_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/")
def index():
    return 'API index'


@app.route("/user")
def user_index():
    return forward_request_to_service(request, USER_SERVICE, "")
