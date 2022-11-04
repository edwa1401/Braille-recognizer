from datetime import datetime
from werkzeug.utils import secure_filename

from webapp.db import db
from webapp.load_image.models import Photo


def create_filename():
    new_filename = f"{str(datetime.now()).replace('.', '_')}.jpg"
    filename = secure_filename(new_filename)
    return filename


def save_upload_info(picture_title, path_to_dir, upload_time):
    upload_info = Photo(picture_title=picture_title, path_to_dir=path_to_dir,
                        upload_time=upload_time)
    db.session.add(upload_info)
    db.session.commit()
