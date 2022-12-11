
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from app.models.user import User


class PostForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.author.choices = [
            (user.id, user.name) for user in User.query.all()
        ]

    title = StringField('Título')
    content = TextAreaField('Conteúdo')
    published = BooleanField('Publicar ?', default=False)
    # author = SelectField('Autores(as)', choices=[(1, 'Leonardo Graciano')])
    author = SelectField('Autores(as)', coerce=str)
    submit = SubmitField('Salvar')
