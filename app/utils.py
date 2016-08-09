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


def authenticate(email, password):
    json_data = {'email': email, 'password': password}
    response = requests.post("http://user/authenticate", json=json_data)
    json_response = response.json()
    if response.status_code >= 300:
        raise CustomError(**json_response)

    return json_response['user']


def identity(payload):
    url = "{}users/{}".format(USER_SERVICE.host, payload['identity'])
    response = requests.get(url)
    print(url)
    json_response = response.json()
    if response.status_code >= 300:
        raise CustomError(**json_response)

    return json_response['user']
