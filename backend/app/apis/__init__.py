from flask import Flask
from app.apis import authAPI, chatAPI


def register_blueprints(app: Flask):
    app.register_blueprint(authAPI.bp)
    app.register_blueprint(chatAPI.bp)
