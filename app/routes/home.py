from flask import Blueprint, render_template

from app.models.post import Post

home = Blueprint("home", __name__)


@home.get('/')
def index():
    posts = Post.query.filter_by(published=True)
    context = {'posts': posts}
    return render_template('home/index.html', **context)
