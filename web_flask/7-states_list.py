#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display a HTML page
    """
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_storage(response_or_exc):
    """teardown storage engine"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
