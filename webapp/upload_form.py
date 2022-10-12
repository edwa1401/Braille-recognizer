from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class Upload_picture_Form(FlaskForm):
    picture = FileField('Фотография:', validators=[FileRequired()])
    submit = SubmitField('Отправить')