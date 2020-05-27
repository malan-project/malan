FROM alpine
RUN apk --no-cache update
RUN apk --no-cache add clamav clamav-libunrar python3 uwsgi uwsgi-python3
RUN freshclam
COPY requirements.txt /etc/requirements.txt
RUN pip3 install -r /etc/requirements.txt

COPY ./server.py /srv/server.py
COPY ./wsgi.py /srv/wsgi.py
COPY ./form.py /srv/form.py
COPY ./static /srv/static
COPY ./templates /srv/templates

COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod o+x /usr/bin/entrypoint.sh

RUN mkdir /var/run/clamav
RUN chown clamav:clamav /var/run/clamav
RUN chmod 750 /var/run/clamav
VOLUME /var/lib/files
EXPOSE 5000
CMD /usr/bin/entrypoint.sh
