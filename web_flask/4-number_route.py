#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ That displays Hello HBNB! """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb_1():
    """ That displays HBNB """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hbnb_2(text):
    """ That displays "C" followed by the value of the text"""
    return("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def hbnb_3(text):
    """ Tthat displays "Python" followed by the value of the text"""
    return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def hbnb_4(n):
    """ That displays "n is a number" """
    return("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
