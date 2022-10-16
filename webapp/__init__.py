from datetime import datetime
from flask import Flask, render_template
from flask_migrate import Migrate
import os
from werkzeug.utils import secure_filename

from webapp.upload_form import Upload_picture_Form
from webapp.model import db, Photo

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/uploader', methods=['POST'])
    def upload_pict():
        form = Upload_picture_Form()
        title = "Braille Recognizer"
        if form.validate_on_submit():
            f = form.picture.data
            file_name = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            upload_time = datetime.now()
            save_upload_info(file_name, app.config['UPLOAD_FOLDER'], upload_time)
            return f'Файл {file_name} загружен'
        return 'Файл не загружен'

    def save_upload_info(picture_title, path_to_dir, upload_time):
        upload_info = Photo(picture_title=picture_title, path_to_dir=path_to_dir,
                            upload_time=upload_time)
        db.session.add(upload_info)
        db.session.commit()
    @app.route('/', methods=['GET'])
    def index():
        form = Upload_picture_Form()
        title = "Braille Recognizer"
        return render_template('upload.html', page_title=title, form=form)

    return app

