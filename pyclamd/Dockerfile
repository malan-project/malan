FROM alpine
COPY requirements.txt /etc/requirements.txt
COPY server.py /srv/server.py
RUN apk --no-cache add clamav clamav-libunrar python3
RUN pip3 install -r /etc/requirements.txt
RUN freshclam
