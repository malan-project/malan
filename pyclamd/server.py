from flask import Flask
import pyclamd
import os

app = Flask(__name__)
#cd = pyclamd.ClamdAgnostic()
cd = pyclamd.ClamdUnixSocket()

if not cd.ping():
  raise Exception('Unable to connect to clamd')

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
