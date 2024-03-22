#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    /: display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    /hbnb: display "HBNB"
    """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c(text):
    """
    /c/<text>: display “C ” followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return f"C {escape(text).replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
