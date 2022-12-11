from ward import test, skip
from tests.fixtures import browser_client
from faker import Faker
from tests.factories.user import UserFactory
from flask import url_for
from app.models.user import User
from flask_login import login_user


@test("shout user look form")
def _(browser=browser_client):

    browser.visit(url_for("post.post_new"))

    assert browser.is_element_present_by_name("csrf_token")
    assert browser.is_element_present_by_name("title")
    assert browser.is_element_present_by_name("content")
    assert browser.is_element_present_by_name("author")
    assert browser.is_element_present_by_name("published")


@test("shout user auth create post with form")
def _(browser=browser_client):

    UserFactory.create(email=Faker().email())
    user = UserFactory()
    login_user(user)

    browser.visit(url_for("post.post_new"))

    title = Faker().name()

    browser.fill('title', title)
    browser.fill('content', Faker().text(max_nb_chars=100))
    browser.select('author', str(user.id))
    browser.check('published')
    browser.find_by_value('Salvar').first.click()

    assert browser.status_code.is_success
    assert browser.is_text_present(title)
