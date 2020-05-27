#!/usr/bin/python3
from flask import Flask, render_template, url_for, redirect, request
import secrets
import pyclamd
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['FILES_PATH'] = '/var/lib/files/'
cd = pyclamd.ClamdAgnostic()

if not cd.ping():
    raise Exception('Unable to connect to clamd')

@app.route('/status')
@app.route('/version')
def status():
    return json.dumps({
        'version': cd.version()
    })

@app.route('/scan/<digest>')
def scan(digest):
    path = app.config['FILES_PATH'] + digest
    desc = cd.scan_file(path)
    status = 'UNSAFE'
    if desc is None:
        status = 'SAFE'
    else:
        desc = desc[path]
        if desc[0] == 'ERROR':
            status = 'ERROR'
            desc = desc[1]
        else:
            desc = desc[1]
    return json.dumps({
        'digest': digest,
        'status': status,
        'desc': desc
    })

@app.route('/', methods=['GET'])
def home():
    return 'pyclamd server home'
