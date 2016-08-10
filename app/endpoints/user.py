from flask import Blueprint, request

from flask_jwt import jwt_required

from app.utils import forward_request_to_service
from app.services import USER_SERVICE

user_service = Blueprint("user_service", __name__)


@user_service.route("/user")
@jwt_required()
def user_index():
    return forward_request_to_service(request, USER_SERVICE, "")


@user_service.route("/signup", methods=["POST"])
def user_signup():
    return forward_request_to_service(request, USER_SERVICE, "/signup")


@user_service.route("/friends")
@jwt_required()
def friends():
    return forward_request_to_service(request, USER_SERVICE, "/friends")
