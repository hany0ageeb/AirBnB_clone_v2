#!/usr/bin/python3
from flask import Flask
"""
script that starts a Flask web application
"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Route: /: display “Hello HBNB!”
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
