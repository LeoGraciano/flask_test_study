import json
from flask import Blueprint, render_template, redirect, url_for, request
from app.forms.post import PostForm
from app.ext import db
from app.models.post import Post
from flask_login import login_required
post = Blueprint("post", __name__)


@login_required
@post.route('/post/<int:id>/', methods=['GET', 'POST', 'DELETE'])
def post_detail(id):
    post = Post.query.get(id)

    if request.method == 'DELETE':
        db.session.delete(post)
        db.session.commit()
        data = {'delete': (url_for('home.index'))}

        return json.dumps(data)

    context = {'post': post}
    return render_template('post/detail.html', **context)


@login_required
@post.route('/post/', methods=['GET', 'POST'])
def post_new():

    form = PostForm()

    if form.validate_on_submit():

        post = Post(
            title=form.title.data, content=form.content.data,
            user_id=form.author.data, published=form.published.data
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('post.post_detail', id=post.id))

    context = {
        'form': form
    }
    return render_template('post/new.html', **context)
