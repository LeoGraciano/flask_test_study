from app.routes.home import home
from app.routes.post import post
from app.routes.auth import auth
from flask import Flask
from dynaconf import FlaskDynaconf


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app, extensions_list=True)

    app.register_blueprint(home)
    app.register_blueprint(post)
    app.register_blueprint(auth)

    return app
