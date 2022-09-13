#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def _hello():
    '''
    Hello Flask
    '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
