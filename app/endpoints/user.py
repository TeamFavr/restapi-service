from flask import Blueprint, request

from app.utils import forward_request_to_service
from app.services import USER_SERVICE

user_service = Blueprint("user_service", __name__)


@user_service.route("/user")
def user_index():
    return forward_request_to_service(request, USER_SERVICE, "")


@user_service.route("/signup", methods=["POST"])
def user_signup():
    return forward_request_to_service(request, USER_SERVICE, "/signup")
