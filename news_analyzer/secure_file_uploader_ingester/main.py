# Main script that combines each function for this module

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import ingester


UPLOAD_FOLDER = '/Users/ashleyrodriguez/Desktop/Spring2021/EC500/news-analyzer-ashrod98/uploads'
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.form.get('option1'):
        return redirect('/ingest_URL')
    if request.form.get('option2'):
        return redirect('/secure_file_uploader_ingester')
    if request.form.get('option1') and equest.form.get('option2'):
        flash('Choose one.')
        return redirect(request.url)
    return ''' 
    <!doctype html>
    <title>Choose new File Type</title>
    <h1>Choose new File Type</h1>
    <h2>Choose one</h2>
    <form method=post enctype=multipart/form-data>
    <input type=checkbox name=option1>
    <label for=option1> Use URL</label><br>
    <input type=checkbox name=option2>
    <label for=option2> Upload PDF</label><br>
    <input type=submit value=Submit>
    </form>
    '''

@app.route('/secure_file_uploader_ingester', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/ingest_URL')
def ingest_weburl():
    if request.form.get['url']:
        flash('No URL')
        return redirect(request.url)
    if request.form['url']:
        return 'Not available'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Submit URL</h1>
    <form method=post enctype=multipart/form-data>
      <input type=text name=url>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



# import logging
# logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')
# possible logging
# logging.info('file {filename} upload start', filename = file_name)
# logging.info('file {filename} upload success', filename = file_name)
# logging.error('file {filename} upload fail', filename = file_name)
# logging.error('Invalid input. File not found')
