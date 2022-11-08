from datetime import datetime
from flask import Blueprint, current_app, flash, render_template
import os

from webapp.load_image.forms import UploadForm
from webapp.load_image.utils import create_filename, save_upload_info
# import predict_cat
# import predict_braille

blueprint = Blueprint("upload", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def index():
    title = "Braille Recognizer"
    upload_form = UploadForm()
    url_photo = "splash_screen.jpg"
    translation_text = "Текст перевода"

    if upload_form.validate_on_submit():
        f = upload_form.image.data
        filename = create_filename()
        f.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        upload_time = datetime.now()
        save_upload_info(filename, current_app.config["UPLOAD_FOLDER"], upload_time)
        flash("Фотография успешно отправлена")
        # its_cat = predict_cat.cat_predict(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        # its_braille = predict_braille.braille_predict(os.path.join(current_app.config["UPLOAD_FOLDER"],
        #                                                            filename))

        # if its_cat:
        #     url_photo = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
        #     translation_text = "Как мило, это же котик! Но пришлите, пожалуйста, фотогафию шрифта Брайля"
        # elif its_braille:
        #     url_photo = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
        #     translation_text = "Что-нибудь"
        # else:
        #    translation_text = "К сожалению, мы не можем обнаружить на этой фотографии шрифт Брайля"

        return render_template("load_image/index.html", page_title=title, form=upload_form,
                               url_photo=url_photo, card_text=translation_text)
    return render_template("load_image/index.html", page_title=title, form=upload_form,
                           url_photo=url_photo, card_text=translation_text)
