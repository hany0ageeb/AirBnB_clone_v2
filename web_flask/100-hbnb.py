#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown(x):
    """teardown sorage"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display a HTML page like 8-index.html
    """
    from models.state import State
    from models.place import Place
    from models.amenity import Amenity
    return render_template(
            '100-hbnb.html',
            states=list(storage.all(State).values()),
            places=list(storage.all(Place).values()),
            amenities=list(storage.all(Amenity).values()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
