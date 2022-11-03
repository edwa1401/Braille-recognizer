from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField, SubmitField


class UploadForm(FlaskForm):
    image = FileField(id="inputGroupFile04",
                      validators=[FileRequired(), FileAllowed(["jpg", "jpeg"], "Только фографии")],
                      render_kw={"class": "form-control"})
    submit = SubmitField("Отправить", render_kw={"class": "btn btn-outline-primary"})
