#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<string:id>', strict_slashes=False)
def states(id=None):
    """Route:  /states
    Route: /states/<id>
    """
    if id:
        states = list(
                filter(
                    lambda state: state.id == id,
                    storage.all(State).values()))
    else:
        states = list(storage.all(State).values())
    return render_template('9-states.html', states=states, state_id=id)


@app.teardown_appcontext
def tear(x):
    """ handle @app.teardown_appcontext"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
