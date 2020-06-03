# malan

uwsgi --plugins-dir /usr/lib/uwsgi --need-plugin python --plugins-list --socket 0.0.0.0:4000 --protocol http -w clamd.wsgi:app
uwsgi --plugins-dir /usr/lib/uwsgi --need-plugin python --plugins-list --socket 0.0.0.0:5000 --protocol http -w malan.wsgi:app
