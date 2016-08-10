import datetime
import requests

from flask import Flask, current_app, jsonify, request

from flask_jwt import JWT

from .endpoints import BLUEPRINTS
from .exceptions import CustomError
from .services import USER_SERVICE
from .settings import SECRET_KEY


jwt = JWT()


@jwt.authentication_handler
def authenticate(email, password):
    json_data = {'email': email, 'password': password}
    response = requests.post("http://user/authenticate", json=json_data)
    json_response = response.json()
    if response.status_code >= 300:
        raise CustomError(**json_response)

    return json_response['user']


@jwt.identity_handler
def identity(payload):
    url = "{}/users/{}".format(USER_SERVICE.host, payload['identity'])
    response = requests.get(url)
    print(url)
    json_response = response.json()
    if response.status_code >= 300:
        raise CustomError(**json_response)

    return json_response['user']


@jwt.jwt_payload_handler
def payload_handler(identity):
    print(identity)
    iat = datetime.datetime.utcnow()
    exp = iat + current_app.config.get('JWT_EXPIRATION_DELTA')
    nbf = iat + current_app.config.get('JWT_NOT_BEFORE_DELTA')
    identity = identity['id']
    return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': identity}


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

    jwt.init_app(app)

    @app.errorhandler(CustomError)
    def custom_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app
