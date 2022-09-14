#!/usr/bin/python3
""" A script that starts a Flask web application """
from sre_parse import State
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_lis', strict_slashes=False)
def states_list():
    """ The state list """
    states = list(storage.all(State).values())
    return(render_template('7-states_list.html', states=states))


@app.teardown_appcontext
def teardown(self):
    """ The method to handle """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
