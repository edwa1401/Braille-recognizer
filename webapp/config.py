import os

basedir = os.path.abspath(os.path.dirname(__file__))


UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '../downloads')
SECRET_KEY = "jwhdjwdhjwdkwhd7672629e292e928e928e"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False