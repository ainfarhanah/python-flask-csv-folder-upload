from flask import Flask, send_file, render_template, request
import os
import glob
import pandas as pd
import datetime
#from werkzeug.import secure file_name
from werkzeug.utils import secure_filename, send_file

app = Flask('__name__')
app.config['UPLOAD_FOLDER'] = 'uploader/'

#index page
@app.route('/')
def index():
    return render_template('index.html')

#upload process
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        files = request.files.getlist("file")

        #save the files in the selected folder
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))


        #return render_template("master.html", data=[res], titles=merge.columns.values, index=False)
        return "Success"
