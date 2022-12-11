from flask import url_for
from ward import test, skip
from faker import Faker
from tests.factories.user import UserFactory
from tests.fixtures import browser_client


@test("should User register in system")
def _(browser=browser_client):
    browser.visit(url_for("home.index"))

    browser.links.find_by_text('Registra-se').click()

    name = Faker().name()
    email = Faker().email()
    password = Faker().password()

    browser.fill("name", name)
    browser.fill("email", email)
    browser.fill("password", password)
    browser.fill("password2", password)

    browser.find_by_value('Registrar').click()

    assert browser.is_text_present("Registro realizado com sucesso")


@test("should User login in system")
def _(browser=browser_client):

    browser.visit(url_for("auth.login"))

    name = Faker().name()
    email = Faker().email()
    password = Faker().password()

    UserFactory(name=name, email=email,
                password=password)

    browser.fill("email", email)
    browser.fill("password", password)
    browser.find_by_value('Login').click()

    assert browser.is_text_present(f"{name}")
    assert browser.is_text_not_present("Login")
    assert browser.is_text_not_present("Registra-se")
