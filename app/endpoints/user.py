from flask import Blueprint, request

from flask_jwt import jwt_required

from app.utils import forward_request_to_service
from app.services import USER_SERVICE

user_service = Blueprint("user_service", __name__)


@user_service.route("/user")
def user_index():
    """

    file: docs/user/user_index.yml

    """
    return forward_request_to_service(request, USER_SERVICE, "")


@user_service.route("/signup", methods=["POST"])
def user_signup():
    return forward_request_to_service(request, USER_SERVICE, "/signup")


@user_service.route("/friends")
@jwt_required()
def friends():
    return forward_request_to_service(request, USER_SERVICE, "/friends")


@user_service.route("/friend-requests", methods=["GET", "POST"])
@jwt_required()
def friend_requests():
    return forward_request_to_service(
        request, USER_SERVICE, "/friend-requests")


@user_service.route("/friendship/<int:id>", methods=["GET", "PATCH", "DELETE"])
@jwt_required()
def friendship_by_id(id):
    return forward_request_to_service(
        request, USER_SERVICE,
        "/friendship/{}".format(id))
