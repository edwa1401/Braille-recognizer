# from webapp.db import db


# class Photo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     picture_title = db.Column(db.String, nullable=False)
#     upload_time = db.Column(db.DateTime, nullable=False)
#     path_to_dir = db.Column(db.String, nullable=False)

#     def __repr__(self):
#         return '<Photo {} {}>'.format(self.picture_title, self.upload_time)