from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import EmailField, SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class UploadPictureForm(FlaskForm):
    picture = FileField('Фотография:',
                        validators=[FileRequired(), FileAllowed(["jpg", "jpeg"],
                                                                "Только фографии формата.jpg или .jpeg ")])
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-outline-primary"})


class ContactForm(FlaskForm):
    name = StringField("Имя", render_kw={"class": "form-control"})
    email = EmailField("Email*", validators=[DataRequired(), Email()],
                       render_kw={"class": "form-control"})
    subject = StringField("Тема обращения", render_kw={"class": "form-control"})
    message = TextAreaField("Текст обращения*", validators=[DataRequired()],
                            render_kw={"class": "form-control"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-outline-primary"})
