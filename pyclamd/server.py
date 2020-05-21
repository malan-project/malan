import os
from flask import Flask, render_template, url_for, redirect, request
import pyclamd
import os

SECRET_KEY= os.urandom(32)
app = Flask(__name__)
#cd = pyclamd.ClamdAgnostic()
cd = pyclamd.ClamdUnixSocket()

if not cd.ping():
  raise Exception('Unable to connect to clamd')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/diagnosis', methods=['GET', 'POST'])
def diagnosis():
    form = FileForm()
    if form.validate_on_submit():
        print('validate post')
        return redirect(url_for('diagnosis'))
    return render_template('diagnosis.html', form=form)

@app.route('/wiki')
def wiki():
    return render_template('wiki.html', search='Search Something')

@app.route('/version')
def status():
    return cd.version()

@app.route('/scan/<path>')
def scan(path):
    path = os.getcwd() + '/' + path
    res = cd.scan_file(path)
    if res is None:
        return f'{path} is clean'
    else:
        return res
