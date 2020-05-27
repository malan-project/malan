#!/usr/bin/python3
from flask import Flask, render_template, url_for, redirect, request
from secrets import token_hex
import os
import hashlib
import tempfile
import shutil

app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(32)
app.config['BLOCK_SIZE'] = 4096
app.config['FILES_PATH'] = '/var/lib/files/'

@app.route('/', methods=['GET'])
def home():
    return 'Malan Gateway Home'

@app.route('/upload', methods=['POST'])
def upload():
    for fname in request.files:
        tfile = tempfile.NamedTemporaryFile(mode='wb', delete=False)
        sha512 = hashlib.sha512()
        while True:
            chunk = request.files[fname].stream.read(app.config['BLOCK_SIZE'])
            if not chunk:
                break
            tfile.write(chunk)
            sha512.update(chunk)
        tfile.close()
        digest = sha512.hexdigest()
        dest_path = app.config['FILES_PATH'] + digest
        shutil.copy(tfile.name, dest_path)
        os.remove(tfile.name)
    return digest

if __name__ == '__main__':
    DEBUG = False
    if 'DEBUG' in os.environ and os.environ['DEBUG'] == '1':
        DEBUG = True
    app.run(host='0.0.0.0', debug=DEBUG)
