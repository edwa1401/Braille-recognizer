from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Имя", render_kw={"class": "form-control"})
    email = EmailField("Email*", validators=[DataRequired(), Email()],
                       render_kw={"class": "form-control"})
    subject = StringField("Тема обращения", render_kw={"class": "form-control"})
    message = TextAreaField("Текст обращения*", validators=[DataRequired()],
                            render_kw={"class": "form-control"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-outline-primary"})
