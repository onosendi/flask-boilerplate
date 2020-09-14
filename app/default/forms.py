from flask_wtf import FlaskForm
from sqlalchemy import func
import wtforms
from wtforms import validators as v

from app.users.models import User


class LoginForm(FlaskForm):
    login = wtforms.StringField(
        validators=[v.DataRequired()])
    password = wtforms.PasswordField(
        validators=[v.DataRequired()])
    remember_me = wtforms.BooleanField()
    submit = wtforms.SubmitField()


class RegisterForm(FlaskForm):
    email = wtforms.StringField(
        validators=[v.DataRequired(), v.Email(), v.Length(max=255)])
    username = wtforms.StringField(
         validators=[v.DataRequired(), v.Length(max=35)])
    password = wtforms.PasswordField(
        validators=[v.DataRequired(), v.Length(min=4)])
    submit = wtforms.SubmitField()

    def validate_email(self, email):
        ''' Make sure the given email is available. '''
        user = User.query\
            .filter(func.lower(User.email) == email.data.lower()).first()
        if user is not None:
            raise v.ValidationError(f'{email.data} is unavailable')

    def validate_username(self, username):
        ''' Make sure the given username is available. '''
        user = User.query\
            .filter(func.lower(User.username) == username.data.lower()).first()
        if user is not None:
            raise v.ValidationError(f'{username.data} is unavailable')
