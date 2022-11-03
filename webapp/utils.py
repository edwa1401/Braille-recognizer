from datetime import datetime
from werkzeug.utils import secure_filename


def create_filename():
    new_filename = f"{str(datetime.now()).replace('.', '_')}.jpg"
    filename = secure_filename(new_filename)
    return filename
