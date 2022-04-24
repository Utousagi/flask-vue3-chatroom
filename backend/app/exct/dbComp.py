import datetime
import time

from peewee import MySQLDatabase, Model
from peewee import CharField, TextField, DateTimeField, ForeignKeyField, BooleanField, TimestampField

from app.utils.nanoIdUtil import nano_id, nano_number_id
from app.config import DATABASE

db = MySQLDatabase('chatroom', **DATABASE.get('dev'))


class _BaseModel(Model):

    class Meta:
        database = db


class User(_BaseModel):
    id = CharField(max_length=32, default=nano_id, primary_key=True)
    username = CharField(unique=True, null=False)
    password = CharField(null=False)
    avatar_url = CharField(null=True)

    class Meta:
        table_name = 'user'


class Room(_BaseModel):
    id = CharField(max_length=32, default=nano_number_id, primary_key=True)
    name = CharField(null=False)
    createTime = DateTimeField(default=datetime.datetime.now)
    description = CharField(null=True)
    private = BooleanField(null=False)
    secret = CharField(null=True)
    owner = ForeignKeyField(User, on_update='cascade', on_delete='cascade')

    class Meta:
        table_name = 'room'


class Message(_BaseModel):
    id = CharField(max_length=32, default=nano_id, primary_key=True)
    content = TextField(null=False)
    postTime = TimestampField(default=time.time)
    user = ForeignKeyField(User, on_update='cascade', on_delete='cascade')
    room = ForeignKeyField(Room, on_update='cascade', on_delete='cascade')

    class Meta:
        table_name = 'message'


if __name__ == '__main__':
    db.connect()
    if not User.table_exists():
        User.create_table()
    if not Room.table_exists():
        Room.create_table()
    if not Message.table_exists():
        Message.create_table()
    db.close()
