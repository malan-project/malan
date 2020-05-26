import os
from flask import Flask, render_template, url_for, redirect, request
from secrets import token_hex
import pyclamd
import os

SECRET_KEY= token_hex(32)
app = Flask(__name__)
#cd = pyclamd.ClamdAgnostic()
cd = pyclamd.ClamdUnixSocket()

if not cd.ping():
    raise Exception('Unable to connect to clamd')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    s_results=[]
    d_results=[]
    form = FileForm()
    if form.validate_on_submit():
        for testfile in form.testfile.data:
            tfname, tfext = os.path.splitext(testfile.filename)
            storedname = os.path.realpath(os.path.curdir) + '/testdata/' + token_hex(8) + tfext
            testfile.save(storedname)
            result = cd.scan_file(storedname)
            if result:
                try:
                    result[testfile.filename] = result.pop(storedname)
                except Exception:
                    assert(False)
                d_results.append(result)
            else:
                s_results.append({testfile.filename: ('SAFE', 'NO')})
            os.remove(storedname)
            del storedname
        return render_template('result.html',
            danger_results=d_results, safe_results=s_results)
    return render_template('main.html', form=form)

@app.route('/wiki')
@app.route('/wiki/')
def wikiMain():
    return render_template('wiki.html', search='Search Something')

@app.route('/wiki/w/<search>')
def wikiIndex(search):
    return render_template('wiki.html', search=search)

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
