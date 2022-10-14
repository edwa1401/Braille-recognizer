from flask import Flask, flash, redirect, render_template, url_for
import os
from werkzeug.utils import secure_filename
from webapp.upload_form import UploadPictureForm, ContactForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    @app.route('/', methods=["GET", "POST"])
    def upload_pict():
        form = UploadPictureForm()
        title = "Braille Recognizer"
        if form.validate_on_submit():
            f = form.picture.data
            file_name = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return render_template("index.html", page_title=title, form=form)

    @app.route("/feedback")
    def feedback():
        title = "Обратная связь"
        contact_form = ContactForm()
        return render_template("feedback.html", page_title=title, form=contact_form)

    @app.route("/feedback-process", methods=["GET", "POST"])
    def feedback_process():
        form = ContactForm()
        if form.validate_on_submit():
            user_name = form.name.data
            user_email = form.email.data
            user_subject = form.subject.data
            user_message = form.message.data
            flash("Ваше обращение отправлено")
        return redirect(url_for("feedback"))

    return app

