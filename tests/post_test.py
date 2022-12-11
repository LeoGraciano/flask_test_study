import json
from flask import url_for
from ward import test, skip
from tests.factories.post import PostFactory
from tests.factories.user import UserFactory
from tests.fixtures import browser_client
from faker import Faker
from app.models.user import User
from flask_login import login_user


@test("shout user auth look new post")
def _(browser=browser_client):

    UserFactory.create(email=Faker().email())
    user = UserFactory()
    login_user(user)

    browser.visit(url_for("home.index"))

    assert browser.status_code.is_success
    assert browser.is_text_present("Novo post")


@skip('Necessário correção do Faker crianção de email')
@test("shout views click links detail")
def _(browser=browser_client):
    posts = PostFactory.create_batch(2)

    browser.visit(url_for("home.index"))

    post = browser.links.find_by_partial_text(posts[1].title)
    post.click()

    assert browser.status_code.is_success
    assert browser.is_text_present(posts[1].content)


@test("shout views detail post")
def _(browser=browser_client):
    p1 = PostFactory.create()

    browser.visit(url_for("post.post_detail", id=p1.id))

    assert browser.status_code.is_success
    assert browser.is_text_present(p1.title)
    assert browser.is_text_present(p1.content)
    assert browser.is_text_present("Publicado")
    assert browser.is_text_present(p1.author.name)
    assert browser.is_element_present_by_value('Excluir')


@test("shout exclude post")
def _(browser=browser_client):
    post = PostFactory.create()

    browser.visit(url_for("post.post_detail", id=post.id))

    btn = browser.find_by_value('Excluir').click()

    url_redirect = json.loads(btn)

    assert browser.status_code.is_success
    assert url_redirect['delete'] == url_for("home.index")
    assert browser.is_text_not_present(post.title)
