from flask import Blueprint, request
from flask_cors import CORS
import app.exct.dbComp as db
from app.exct.authComp import auth
from app.utils.httpUtil import success, parse_request

bp = Blueprint('chat-api', __name__, url_prefix='/api/chat')
cors = CORS(bp, expose_headers='access_token')


@bp.route('getMessage', methods=['GET'])
@auth.login_required
def get_message():
    time = int(request.args.get('time'))
    room_id = request.args.get('roomId')
    message = db.Message.select().where((db.Message.room == room_id) & (db.Message.postTime < time))\
        .order_by(db.Message.postTime.desc()).limit(10)
    message = [{'time': m.postTime,
                'content': m.content,
                'username': m.user.username,
                'avatar': m.user.avatar_url} for m in message]
    message.reverse()
    return success('成功', message)


@bp.route('checkRoomExist', methods=['GET'])
def check_room_exist():
    room_id = request.args.get('roomId')
    room = db.Room.get_or_none(db.Room.id == room_id)
    if room is None:
        return success('房间不存在')
    return success('房间存在', {'name': room.name})


@bp.route('createRoom', methods=['POST'])
@auth.login_required
def create_room():
    uid = auth.current_user()
    data = parse_request(request)
    name = data.get('name')
    description = data.get('description')
    private = data.get('private')
    secret = data.get('secret') if private else ""
    room = db.Room.create(name=name, description=description, private=private, secret=secret, owner=uid)
    return success('创建成功', {'id': room.id})


@bp.route('listRoom', methods=['GET'])
@auth.login_required
def list_room():
    rooms = db.Room.select().order_by(db.Room.createTime.desc())
    rooms = [{'id': r.id,
              'name': r.name,
              'description': r.description,
              'createTime': r.createTime.strftime('%Y-%m-%d %H:%M:%S'),
              'private': '是' if r.private else '否'} for r in rooms]
    return success('成功', rooms)


@bp.route('searchRoom', methods=['GET'])
@auth.login_required
def search_room():
    keyword = request.args.get('keyword')
    rooms = db.Room.select().where((db.Room.name.contains(keyword)) | (db.Room.id == keyword))\
        .order_by(db.Room.createTime.desc())
    rooms = [{'id': r.id,
              'name': r.name,
              'description': r.description,
              'createTime': r.createTime.strftime('%Y-%m-%d %H:%M:%S'),
              'private': '是' if r.private else '否'} for r in rooms]
    return success('成功', rooms)
