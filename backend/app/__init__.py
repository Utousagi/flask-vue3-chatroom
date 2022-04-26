from flask import Flask
import app.apis.authAPI
from app.exct import register_components
from app.apis import register_blueprints
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    register_blueprints(app)
    register_components(app)
    CORS(app, expose_headers='access_token')

    @app.route('/')
    def index():
        return 'Hello!'

    return app


app = create_app()
