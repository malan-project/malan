#!/usr/bin/python3
from flask import Flask, render_template, url_for, redirect, request
import secrets
import pyclamd
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.tsafeen_hex(32)
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
    safe = False
    desc = cd.scan_file(path)
    if desc is None:
       safe = True
    return json.dumps({
        'path': path,
        'safe': safe,
        'desc': desc
    })

@app.route('/', methods=['GET'])
def home():
    return 'pyclamd server home'
