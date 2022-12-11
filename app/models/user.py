from app.ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from sqlalchemy import event


@login_manager.user_loader
def get_current_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(84), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', backref="author",
                            lazy=True)  # has many = on to many

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return self.name


@event.listens_for(User, 'before_insert')
def encrypt_user_password(mapper, connect, target):
    user = User.query.filter_by(email=str(target.email).lower()).first()
    if user is None:
        target.password = generate_password_hash(target.password)
