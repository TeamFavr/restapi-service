from flask import Blueprint, request

from flask_jwt import jwt_required

from flasgger.utils import swag_from

from app.utils import forward_request_to_service
from app.services import USER_SERVICE

user_service = Blueprint("user_service", __name__)


@user_service.route("/user")
@swag_from('/code/docs/user/user_index.yml', methods=['GET'])
def user_index():
    """User Index."""
    return forward_request_to_service(request, USER_SERVICE, "")


@user_service.route("/signup", methods=["POST"])
@swag_from('/code/docs/user/user_signup.yml', methods=['GET'])
def user_signup():
    """User Signup Route."""
    return forward_request_to_service(request, USER_SERVICE, "/signup")


@user_service.route("/friends")
@jwt_required()
@swag_from('/code/docs/user/user_friends.yml', methods=['GET'])
def friends():
    """List all of the current users friends."""
    return forward_request_to_service(request, USER_SERVICE, "/friends")


@user_service.route("/friend-requests", methods=["GET", "POST"])
@jwt_required()
@swag_from('/code/docs/user/user_friend_requests_get.yml', methods=['GET'])
@swag_from('/code/docs/user/user_friend_requests_post.yml', methods=['POST'])
def friend_requests():
    return forward_request_to_service(
        request, USER_SERVICE, "/friend-requests")


@user_service.route("/friendship/<int:id>", methods=["GET", "PATCH", "DELETE"])
@jwt_required()
@swag_from('/code/docs/user/user_friendship_get.yml', methods=['GET'])
@swag_from('/code/docs/user/user_friendship_patch.yml', methods=['PATCH'])
@swag_from('/code/docs/user/user_friendship_delete.yml', methods=['DELETE'])
def friendship_by_id(id):
    return forward_request_to_service(
        request, USER_SERVICE,
        "/friendship/{}".format(id))
