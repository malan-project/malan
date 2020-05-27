import os
from .app import app
if __name__ == '__main__':
    DEBUG = False
    if 'DEBUG' in os.environ and os.environ['DEBUG'] == '1':
        DEBUG = True
        app.run(host='0.0.0.0', debug=DEBUG)
