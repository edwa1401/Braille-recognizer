from webapp.db import db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=True)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Message from {self.email}"
