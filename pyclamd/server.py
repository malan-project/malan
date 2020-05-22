import os
from flask import Flask, render_template, url_for, redirect, request
from secrets import token_hex
import pyclamd
from form import FileForm


SECRET_KEY= os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
cd = pyclamd.ClamdAgnostic()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/diagnosis', methods=['GET', 'POST'])
def diagnosis():
    results=[]
    form = FileForm()
    if form.validate_on_submit():
        for testfile in form.testfile.data:
            if(testfile):
                tfname , tfext = os.path.splitext(testfile.filename)
                storedname = os.path.realpath(os.path.curdir) + '/testdata/' + token_hex(8) + tfext
                testfile.save(storedname)
                result = cd.scan_file(storedname)
                if result:
                    try:
                        result[testfile.filename] = result.pop(storedname)
                    except Exception:
                        assert(False)
                print(result)
                results.append(result)
                os.remove(storedname)
                del storedname
        return render_template('result.html', results=results)
    return render_template('diagnosis.html', form=form)

@app.route('/wiki')
def wiki():
    return render_template('wiki.html', search='Search Something')

@app.route('/version')
def version():
    return render_template('version.html', cd=cd)

if __name__ == '__main__':
    app.run(debug=True)
