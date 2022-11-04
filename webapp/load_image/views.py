from datetime import datetime
from flask import Blueprint, current_app, flash, render_template
import os

from webapp.load_image.forms import UploadForm
from webapp.load_image.utils import create_filename, save_upload_info

blueprint = Blueprint("upload", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def index():
    title = "Braille Recognizer"
    upload_form = UploadForm()
    url_photo = os.path.join(current_app.config["UPLOAD_FOLDER"], "photo.jpg")
    translation_text = "Текст перевода"
    if upload_form.validate_on_submit():
        f = upload_form.image.data
        filename = create_filename()
        f.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        upload_time = datetime.now()
        save_upload_info(filename, current_app.config["UPLOAD_FOLDER"], upload_time)
        flash("Фотография успешно отправлена")

        return render_template("load_image/index.html", page_title=title, form=upload_form,
                               url_photo=url_photo, card_text=translation_text)
    return render_template("load_image/index.html", page_title=title, form=upload_form,
                           url_photo=url_photo, card_text=translation_text)
