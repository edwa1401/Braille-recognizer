from flask import Flask
from flask_migrate import Migrate

from webapp.db import db
from webapp.feedback.views import blueprint as feedback_blueprint
from webapp.load_image.views import blueprint as load_image_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(feedback_blueprint)
    app.register_blueprint(load_image_blueprint)

    return app
