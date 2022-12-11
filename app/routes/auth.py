from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_manager, login_user
from app.ext import db
from app.forms.auth import LoginForm, RegisterForm
from app.models.user import User

auth = Blueprint("auth", __name__)


@auth.route('/register/', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        name = form.name.data
        email = str(form.email.data).lower()
        password = form.password.data

        user = User(
            name=name,
            email=email,
            password=password
        )
        db.session.add(user)
        db.session.commit()

        flash("Registro realizado com sucesso")

        return redirect(url_for('home.index'))

    context = {
        'form': form
    }

    return render_template('auth/register.html', **context)


@auth.route('/login/', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            login_user(user)

        flash(f"Bem vindo, {user.name}")

        return redirect(url_for('home.index'))

    context = {
        'form': form
    }

    return render_template('auth/login.html', **context)
