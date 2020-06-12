FROM ubuntu

VOLUME /var/lib/files
EXPOSE 8080

RUN apt update
RUN apt install -y python3 python3-pip uwsgi uwsgi-plugin-python3

COPY requirements.txt /etc/requirements.txt
RUN pip3 install -r /etc/requirements.txt

COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod o+x /usr/bin/entrypoint.sh
CMD /usr/bin/entrypoint.sh

COPY ./__init__.py /srv/__init__.py
COPY ./app.py /srv/app.py
COPY ./wsgi.py /srv/wsgi.py
COPY ./malan_net.py /srv/malan_net.py
COPY ./checkpoint.pth /srv/checkpoint.pth

VOLUME /var/lib/images
