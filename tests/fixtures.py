from splinter import Browser
from ward import fixture

from app import create_app
from app.ext import db


@fixture
def browser_client():
    app = create_app()
    app_context = app.test_request_context()
    app.testing = True
    app_context.push()

    browser = Browser("flask", app=app)

    with app.test_client():
        db.create_all()
        yield browser

    db.session.remove()
    db.drop_all()
