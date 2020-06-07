## introduction
![malan_logo](https://github.com/malan-project/malan/blob/master/malan_svc/static/images/logo.png)
*malan is 

## how to start
+ requires
uwsgi --plugins-dir /usr/lib/uwsgi --need-plugin python --plugins-list --socket 0.0.0.0:4000 --protocol http -w clamd.wsgi:app
uwsgi --plugins-dir /usr/lib/uwsgi --need-plugin python --plugins-list --socket 0.0.0.0:5000 --protocol http -w malan.wsgi:app


## pull request

## make issue

## coding convention rule
+ python
+ javascript
+ Dockerfile

## LICENSE
[license.txt](https://github.com/malan-project/malan/blob/master/LICENSE)
