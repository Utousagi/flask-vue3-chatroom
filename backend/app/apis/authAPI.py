from flask import Blueprint, request, make_response
from flask_cors import CORS
from app.utils.httpUtil import *
from app.utils.bcryptUtil import *
import app.exct.dbComp as db
from app.exct.authComp import auth, generate_token

bp = Blueprint('auth-api', __name__, url_prefix='/api/auth')
cors = CORS(bp, expose_headers='access_token')


@bp.route('/login', methods=['POST'])
def login():
    data = parse_request(request)
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    user = db.User.select().where(db.User.username == username).first()
    if not user or not compare_pwd(password, user.password):
        return make_response(param_err('用户名或密码错误'))
    token = generate_token(user.id)
    user = {'username': user.username, 'avatar': user.avatar_url}
    response = make_response(success('登录成功', user))
    response.headers['access_token'] = token
    return response


@bp.route('/register', methods=['POST'])
def register():
    data = parse_request(request)
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    if db.User.select().where(db.User.username == username):
        return make_response(param_err('用户名已存在'))
    user = db.User.create(username=username, password=hash_pwd(password))
    if not user:
        return make_response(server_err('内部错误，创建失败'))
    token = generate_token(user.id)
    user = {'username': user.username, 'avatar': user.avatar_url}
    response = make_response(success('注册成功，将自动跳转', user))
    response.headers['access_token'] = token
    return response

