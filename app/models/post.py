from app.ext import db
from app.models.user import User


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, default=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False
    )

    def __repr__(self):
        return '<Post %r>' % self.title

    def __str__(self):
        return self.title
