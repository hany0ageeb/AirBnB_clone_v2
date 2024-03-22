#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
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
    /hbnb: display “HBNB”
    """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c(text):
    """
    /c/<text>: display “C ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text='is cool'):
    """
    display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return f"Python {escape(text).replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    /number/<n>: display “n is a number” only if n is an integer
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
     display a HTML page only if n is an integer
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
