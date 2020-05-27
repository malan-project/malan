#!/usr/bin/python3
from flask import Flask, render_template, url_for, redirect, request
import secrets
import os
import json
import magic

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['FILES_PATH'] = '/var/lib/files/'

@app.route('/status')
@app.route('/version')
def status():
    return json.dumps({
        'version': magic.version()
    })

@app.route('/scan/<digest>')
def scan(digest):
    path = app.config['FILES_PATH'] + digest
    magic_val = None
    mime = None
    status = 'SUCCESS'
    error = None
    try:
        magic_val = magic.from_file(path)
        mime = magic.from_file(path, mime=True) 
    except Exception as e:
        status = 'ERROR'
        error = str(e)
    return json.dumps({
        'status': status,
        'error': error,
        'digest': digest,
        'magic': magic_val,
        'mime': mime
    })

@app.route('/', methods=['GET'])
def home():
    return 'Magic server home'
