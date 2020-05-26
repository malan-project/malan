/usr/sbin/clamd
uwsgi --plugins-dir /usr/lib/uwsgi --need-plugin python3 --plugins-list --socket 0.0.0.0:5000 --protocol http --chdir /srv -w wsgi:app
