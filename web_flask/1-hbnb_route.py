#!/usr/bin/python3
"""
This script starts a flask web application listening
on 0.0.0.0, port 5000
Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
