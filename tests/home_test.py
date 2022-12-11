from flask import url_for
from ward import test, skip
from tests.factories.post import PostFactory
from tests.fixtures import browser_client
from faker import Faker


@test("shout visitor page home with successful")
def _(browser=browser_client):

    browser.visit(url_for("home.index"))

    assert browser.status_code.is_success
    assert browser.is_text_present("Home Page")


@skip('Necessário correção do Faker crianção de email')
@test("shout views all posts")
def _(browser=browser_client):
    posts = PostFactory.create_batch(5)

    browser.visit(url_for("home.index"))

    assert browser.status_code.is_success
    for post in posts:
        assert browser.is_text_present(post.title)


@skip('Necessário correção do Faker crianção de email')
@test("shout views active posts")
def _(browser=browser_client):

    p1 = PostFactory.create()
    p2 = PostFactory.create(title="Test", published=False)

    browser.visit(url_for("home.index"))

    assert browser.status_code.is_success
    assert browser.is_text_not_present(p2.title)
    assert browser.is_text_present(p1.title)
