from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker
from app.models.user import User
from app.ext import db


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    name = Faker().name()
    email = Faker().email()
    password = Faker().password()
