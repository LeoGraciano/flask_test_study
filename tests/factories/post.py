import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker

from app.ext import db
from app.models.post import Post
from tests.factories.user import UserFactory


class PostFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'
        sqlalchemy_get_or_create = ('title',)

    title = Faker().name()
    content = Faker().text(max_nb_chars=100)
    published = True
    author = factory.SubFactory(UserFactory)
