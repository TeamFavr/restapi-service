import requests

from .exceptions import CustomError
from .services import USER_SERVICE


def forward_request_to_service(request, service, endpoint):
    url = "{}{}".format(service.host, endpoint)
    request_method = getattr(requests, request.method.lower())
    headers = request.headers
    params = request.args
    resp = request_method(url, params=params, json=request.json,
                          headers=headers)

    return resp.text, resp.status_code
