from flask import Flask, render_template
import os
from werkzeug.utils import secure_filename
from webapp.upload_form import Upload_picture_Form


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    @app.route('/uploader', methods=['POST'])
    def upload_pict():
        form = Upload_picture_Form()
        title = "Braille Recognizer"
        if form.validate_on_submit():
            f = form.picture.data
            file_name = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            return 'Файл загружен'
        return 'Файл не загружен'

    @app.route('/', methods=['GET'])
    def index():
        form = Upload_picture_Form()
        title = "Braille Recognizer"
        return render_template('upload.html', page_title=title, form=form)

    return app

