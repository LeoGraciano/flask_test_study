
from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from wtforms import (
    EmailField, PasswordField,
    StringField, SubmitField
)

from wtforms.validators import ValidationError, DataRequired

from app.models.user import User


class RegisterForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = StringField('Nome completo', validators=[DataRequired()])
    email = EmailField('E-Mail', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Confirmar senha', validators=[DataRequired()])

    submit = SubmitField('Registrar')

    def validate_password(self, password):
        if password.data != self.password2.data:
            raise ValidationError('Senha incorreta')


class LoginForm(FlaskForm):

    email = EmailField('E-Mail', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])

    submit = SubmitField('Login')

    def validate_email(self, email):
        if not email.data:
            raise ValidationError('Email invalido')
        return email.data

    def validate_password(self, password):
        if not password.data:
            raise ValidationError('Senha Invalida')

        return password.data

    def validate(self, extra_validators=None):
        user = User.query.filter_by(email=str(self.email.data).lower()).first()
        if not user \
                or not check_password_hash(user.password, self.password.data):
            raise ValidationError('Email/senha invalido')

        return super().validate(extra_validators)
