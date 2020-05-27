#!/usr/bin/python3
from flask import Flask, render_template, url_for, redirect, request
from secrets import token_hex
import os
import hashlib
import tempfile
import shutil
import json
import requests
from .lib.form import FileForm

app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(32)
app.config['BLOCK_SIZE'] = 4096
app.config['FILES_PATH'] = '/var/lib/files'

# CLAMD 서버의 주소
app.config['CLAMD_URL'] = 'http://localhost:4000'

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """
        유저가 방문하는 메인 페이지입니다.
        드래그-드롭 또는 파일 입력을 받기 위해 GET, POST메소드를 모두 사용합니다.
        아래 알고리즘, 특히 if form.validate_on_submit(): 하위구문은
        POST방식으로 파일을 받았을 때의 실행을 명시합니다.
            서버에 파일을 업로드하면
            서버는 이를 /var/lib/(SHA512 hash)
            에 저장하고 clamav를 실행합니다.
            실행 결과는
            s_result(안전한 파일 목록, (*필요시)추가 데이터),
            d_result(위험한 파일 목록, 파일 위험요소, (*필요시)추가 데이터)에
            저장됩니다.
            결과 페이지에서 표시될 데이터를 바꾸고 싶으면
            아래 부분에 작성하시면 됩니다.
            표시하고 싶은 범주를 바꾸고 싶으시면
            templates/result.html >> thead >> th 목록을 바꾸면 됩니다.
        GET 방식으로 접근했을 때, 즉 단순히 페이지에 접근했을 때는
        메인 페이지를 보여줍니다.
    """
    s_results=[]
    d_results=[]
    form = FileForm()
    if form.validate_on_submit():
        for test_file in form.test_file.data:
            digest = upload_file(test_file.stream)
            scan_res = scan_file(digest)
            if scan_res['status'] == 'SAFE':
                s_results.append({test_file.filename: ('SAFE', 'NO')})
            elif scan_res['status'] == 'UNSAFE':
                d_results.append({test_file.filename: ('UNSAFE', scan_res['desc'])})

        return render_template('result.html',
             danger_results=d_results, safe_results=s_results)

    return render_template('main.html', form=form)

@app.route('/wiki')
@app.route('/wiki/')
def wikiMain():
    """
        위키 사이트의 메인 페이지로 사용할 라우트입니다.
    """
    return render_template('wiki.html', search='Search Something')

@app.route('/wiki/w/<search>')
def wikiIndex(search):
    """
        위키 사이트의 각 항목을 표시하는데 사용할 라우트입니다.
    """
    return render_template('wiki.html', search=search)


@app.route('/upload', methods=['POST'])
def upload():
    for fname in request.files:
        digest = upload_file(request.files[fname].stream)
    return json.dumps({'digest': digest})

def upload_file(stream):
    tfile = tempfile.NamedTemporaryFile(mode='wb', delete=False)
    sha512 = hashlib.sha512()
    while True:
        chunk = stream.read(app.config['BLOCK_SIZE'])
        if not chunk:
            break
        tfile.write(chunk)
        sha512.update(chunk)
    tfile.close()
    digest = sha512.hexdigest()
    dfile = app.config['FILES_PATH'] + '/' + digest
    shutil.copy(tfile.name, dfile)
    os.chmod(dfile, 444)
    os.remove(tfile.name)
    return digest

def scan_file(digest):
    return json.loads(requests.get(app.config['CLAMD_URL'] + '/' + 'scan' + '/' + digest).text)
