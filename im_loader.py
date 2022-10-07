from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = r'C:\projects\braille_recognizer\pictures'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_pict():
   if request.method == 'POST':
      f = request.files['file']
      #fl = secure_filename(f.filename)
      #f.save(secure_filename(f.filename)))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)