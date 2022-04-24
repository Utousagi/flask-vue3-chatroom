from flask_socketio import SocketIO, join_room, leave_room
import app.exct.dbComp as db

socket = SocketIO()


@socket.on('connect')
def connect():
    print('connected')


@socket.on('disconnect')
def disconnect():
    print('disconnect')


@socket.on('user_login')
def user_login(username: str):
    print(f'{username} login')


@socket.on('join_room')
def on_join(username: str, room_id: str):
    join_room(room_id)
    print(f'{username} join {room_id}')


@socket.on('leave_room')
def on_leave(username: str, room_id: str):
    print(f'{username} leave {room_id}')
    leave_room(room_id)


@socket.on('send_message')
def handle_message(content: str, username: str, avatar: str, room_id: str):
    message = {'content': content,
               'username': username,
               'avatar': avatar}
    socket.emit('broadcast_message', message, room=room_id)
    db.db.connect()
    uid = db.User.get(db.User.username == username).id
    db.Message.create(content=content, user_id=uid, room_id=room_id)
    db.db.close()
