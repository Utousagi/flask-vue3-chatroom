import time

from flask import make_response
from flask_httpauth import HTTPTokenAuth
from authlib.jose import jwt, JoseError
from app.config import SECRET_KEY
from app.utils.httpUtil import auth_err

auth = HTTPTokenAuth(scheme='Bearer')


def generate_token(uid: str):
    header = {'alg': 'HS256'}
    key = SECRET_KEY
    now = time.time()
    data = {'nbf': now, 'exp': now+60*60*24*7, 'uid': uid}
    token = jwt.encode(header, data, key)
    return token


@auth.verify_token
def verify_token(token: str):
    key = SECRET_KEY
    try:
        claim = jwt.decode(s=token, key=key)
        claim.validate()
    except JoseError as e:
        print(e.error)
        return False
    return claim.get('uid')


def unauthorized():
    return make_response(auth_err(), 401)
