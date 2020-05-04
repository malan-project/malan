from flask import Flask
import pyclamd

app = Flask(__name__)
cd = pyclamd.ClamdAgnostic()

@app.route('/version')
def status():
  if cd.ping():
    return cd.version()
  else:
    'Unable to connect to clamd'
