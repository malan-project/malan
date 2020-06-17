FROM alpine

VOLUME /var/lib/files
EXPOSE 8080

RUN apk --no-cache update
RUN apk --no-cache add python3 uwsgi uwsgi-python3 py3-pip

COPY requirements.txt /etc/requirements.txt
RUN pip3 install -r /etc/requirements.txt

COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod o+x /usr/bin/entrypoint.sh
CMD /usr/bin/entrypoint.sh

COPY ./__init__.py /srv/__init__.py
COPY ./app.py /srv/app.py
COPY ./wsgi.py /srv/wsgi.py

RUN apk --no-cache add clamav clamav-libunrar
RUN freshclam

RUN mkdir /var/run/clamav
RUN chown clamav:clamav /var/run/clamav
RUN chmod 750 /var/run/clamav
