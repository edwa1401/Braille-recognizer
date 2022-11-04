import os

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "../downloads")
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")
SECRET_KEY = "nruefur47h5nit58h4uu73h7^E%F^juehf"
