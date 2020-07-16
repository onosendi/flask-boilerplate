from flask_wtf import FlaskForm
import wtforms
from wtforms import validators as v


class PostForm(FlaskForm):
    body = wtforms.StringField(
        'What\'s on your mind?',
        validators=[v.DataRequired(), v.Length(max=255)]
    )
    submit = wtforms.SubmitField('Post')
