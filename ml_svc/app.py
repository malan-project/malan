#!/usr/bin/python3
from flask import Flask
import secrets
import os
import json
import numpy as np
import PIL.Image

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['FILES_PATH'] = '/var/lib/files/'
app.config['IMAGES_PATH'] = '/var/lib/images/'

@app.route('/status')
@app.route('/version')
def status():
    return json.dumps({
        'version': '0.0.1'
    })

@app.route('/convert/<digest>')
def scan(digest):
    try:
        ORI_WIDTH = 4096
        IMAGE_SIZE = (32, 32)
        path = app.config['FILES_PATH'] + digest
        data = np.fromfile(path, dtype='uint8')
        if data.shape[0] % ORI_WIDTH != 0:
            data = np.pad(data, (0, ORI_WIDTH - f.shape[0] % ORI_WIDTH))
        data = data.reshape((-1, ORI_WIDTH))
        image_path = app.config['IMAGES_PATH'] + digest + '.png'
        image = PIL.Image.fromarray(data)
        image = image.resize(IMAGE_SIZE, PIL.Image.NEAREST)
        image.save(image_path)
        status = 'SUCCESS'
        error = None
    except Exception as e:
        status = 'ERROR'
        error = str(e)
    return json.dumps({
        'status': status,
        'error': error,
        'digest': digest,
    })

@app.route('/', methods=['GET'])
def home():
    return 'ML server home'
