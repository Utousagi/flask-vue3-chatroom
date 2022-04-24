from http import HTTPStatus

from flask import Request, json, jsonify


def parse_request(req: Request):
    data: dict = json.loads(req.get_data().decode('utf-8'))
    return data


def _http_response(code, message, data):
    return jsonify({'code': code, 'message': message, 'data': data})


def success(message='', data=None):
    return _http_response(HTTPStatus.OK, message, data)


def param_err(message='', data=None):
    return _http_response(HTTPStatus.BAD_REQUEST, message, data)


def auth_err(message='', data=None):
    return _http_response(HTTPStatus.UNAUTHORIZED, message, data)


def server_err(message='', data=None):
    return _http_response(HTTPStatus.INTERNAL_SERVER_ERROR, message, data)
