#! /bin/bash

sudo docker cp clamd_svc/__init__.py malan_clamd_1:/srv/__init__.py
sudo docker cp clamd_svc/app.py malan_clamd_1:/srv/app.py
sudo docker cp clamd_svc/wsgi.py malan_clamd_1:/srv/wsgi.py

sudo docker cp magic_svc/__init__.py malan_magic_1:/srv/__init__.py
sudo docker cp magic_svc/app.py malan_magic_1:/srv/app.py
sudo docker cp magic_svc/wsgi.py malan_magic_1:/srv/wsgi.py

sudo docker cp malan_svc/__init__.py malan_malan_1:/srv/__init__.py
sudo docker cp malan_svc/app.py malan_malan_1:/srv/app.py
sudo docker cp malan_svc/wsgi.py malan_malan_1:/srv/wsig.py
sudo docker cp malan_svc/lib malan_malan_1:/srv/lib
sudo docker cp malan_svc/static malan_malan_1:/srv/static
sudo docker cp malan_svc/templates malan_malan_1:/srv/templates

sudo docker cp ml_svc/__init__.py malan_ml_1:/srv/__init__.py
sudo docker cp ml_svc/app.py malan_ml_1:/srv/app.py
sudo docker cp ml_svc/wsgi.py malan_ml_1:/srv/wsgi.py
sudo docker cp ml_svc/malan_net.py malan_ml_1:/srv/malan_net.py
sudo docker cp ml_svc/checkpoint.pth malan_ml_1:/srv/checkpoint.pth

sudo docker-compose build
