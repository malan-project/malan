#!/usr/bin/python3
from flask import Flask, render_template, url_for, redirect, request
from secrets import token_hex
import pyclamd
import os
from form import FileForm
SECRET_KEY= token_hex(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
#cd = pyclamd.ClamdAgnostic()
cd = pyclamd.ClamdUnixSocket()

if not cd.ping():
    raise Exception('Unable to connect to clamd')

@app.route('/version')
def status():
    return render_template('version.html', cd=cd)

@app.route('/scan/<path>')
def scan(path):
    path = os.getcwd() + '/' + path
    res = cd.scan_file(path)
    if res is None:
        return f'{path} is clean'
    else:
        return res

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """
        유저가 방문하는 메인 페이지입니다.
        드래그-드롭 또는 파일 입력을 받기 위해 GET, POST메소드를 모두 사용합니다.
        아래 알고리즘, 특히 if form.validate_on_submit(): 하위구문은
        POST방식으로 파일을 받았을 때의 실행을 명시합니다.
            서버에 파일을 업로드하면
            서버는 이를 testdata/(랜덤 8자 hex).(원본 확장자)
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

if __name__ == '__main__':
    """
    host='0.0.0.0'을 사용하면 로컬호스트 외의 환경에서도 사용할 수 있다고 합니다.
    debug=True 옵션을 사용하면 프로젝트 파일 변경이 즉각적으로 서버에 반영됩니다.
    다만 버그가 있다면 서버를 통해 프로젝트 파일을 수정할 수도 있으므로
    반드시 배포시에는 debug=False 옵션을 사용해야 합니다.
    """
    app.run(host='0.0.0.0', debug=False)
