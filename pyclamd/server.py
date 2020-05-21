import os
from flask import Flask, render_template, url_for, redirect, request
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
    form = FileForm()
    if form.validate_on_submit():
        print('validate post')
        return redirect(url_for('diagnosis'))
    return render_template('diagnosis.html', form=form)

@app.route('/wiki')
def wiki():
    return render_template('wiki.html', search='Search Something')

@app.route('/version')
def version():
    return render_template('version.html', cd=cd)

if __name__ == '__main__':
    app.run(debug=True)
