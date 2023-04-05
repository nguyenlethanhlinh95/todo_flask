from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=6, max=255)])
    content = StringField('content', validators=[DataRequired(), Length(min=6, max=255)])
