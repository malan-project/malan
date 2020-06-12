#!/usr/bin/python3
from flask import Flask
import secrets
import os
import json
import numpy as np
import PIL.Image
import torch
import torch.nn as nn
from .malan_net import MalanNet

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
ORI_WIDTH = 4096
IMAGE_SIZE = (32, 32)

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['FILES_PATH'] = '/var/lib/files/'
app.config['IMAGES_PATH'] = '/var/lib/images/'
app.config['CHECKPOINT_PATH'] = '/srv/checkpoint.pth'

model = MalanNet()
model.load_state_dict(torch.load(app.config['CHECKPOINT_PATH'])['state_dict'])
model.eval()

@app.route('/', methods=['GET'])
def home():
    return 'ML server home'

@app.route('/status')
@app.route('/version')
def status():
    return json.dumps({
        'version': '0.0.1'
    })

@app.route('/convert/<digest>')
def convert(digest):
    try:
        status = 'SUCCESS'
        error = None
        path = app.config['FILES_PATH'] + digest
        data = np.fromfile(path, dtype='uint8')
        if data.shape[0] % ORI_WIDTH != 0:
            data = np.pad(data, (0, ORI_WIDTH - data.shape[0] % ORI_WIDTH))
        data = data.reshape((-1, ORI_WIDTH))
        image_path = app.config['IMAGES_PATH'] + digest + '.png'
        image = PIL.Image.fromarray(data)
        image = image.resize(IMAGE_SIZE, PIL.Image.NEAREST)
        image.save(image_path)
    except Exception as e:
        status = 'ERROR'
        error = str(e)
    return json.dumps({
        'status': status,
        'error': error,
        'digest': digest,
    })

@app.route('/scan/<digest>')
def scan(digest):
    try:
        status = 'SAFE'
        error = None
        path = app.config['IMAGES_PATH'] + digest + '.png'
        data = torch.from_numpy(np.array(PIL.Image.open(path)))
        res = model(data.view(1, 1, IMAGE_SIZE[0], IMAGE_SIZE[1]).float())
        if (res > 0.5).item() == True:
           status = 'UNSAFE' 
    except Exception as e:
        status = 'ERROR'
        error = str(e)
    return json.dumps({
        'status': status,
        'error': error,
        'digest': digest,
        'danger': res.item()
    })
