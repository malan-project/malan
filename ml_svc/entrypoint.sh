uwsgi --master --plugins-dir /usr/lib/uwsgi --need-plugin python3 --plugins-list --socket 0.0.0.0:8080 --protocol http -w srv.wsgi:app
