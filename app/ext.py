from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def init_app(app):
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
