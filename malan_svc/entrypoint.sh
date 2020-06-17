uwsgi --master --plugins-dir /usr/lib/uwsgi/plugins --need-plugin python3 --socket 0.0.0.0:8080 --protocol http -w srv.wsgi:app
