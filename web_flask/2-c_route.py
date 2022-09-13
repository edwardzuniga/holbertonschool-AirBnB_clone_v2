#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ That displays Hello HBNB! """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ That displays HBNB """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hbnb_1(text):
    """ That displays "C" followed by the value of the text"""
    return("C {}".format(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
