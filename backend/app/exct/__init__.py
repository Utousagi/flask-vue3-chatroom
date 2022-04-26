from flask import Flask
from app.exct.socketComp import socket
from app.exct.dbComp import db


def register_components(app: Flask):
    socket.init_app(app, cors_allowed_origins='*', port=5000)

    @app.before_request
    def connect_db():
        db.connect()

    @app.after_request
    def close_db(response):
        db.close()
        return response
