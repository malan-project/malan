FROM alpine

VOLUME /var/lib/files
EXPOSE 8080

RUN apk --no-cache update
RUN apk --no-cache add python3 uwsgi uwsgi-python3

COPY requirements.txt /etc/requirements.txt
RUN pip3 install -r /etc/requirements.txt
CMD /usr/bin/entrypoint.sh

COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod o+x /usr/bin/entrypoint.sh

COPY ./__init__.py /srv/__init__.py
COPY ./app.py /srv/app.py
COPY ./wsgi.py /srv/wsgi.py
COPY ./lib /srv/lib
COPY ./static /srv/static
COPY ./templates /srv/templates
