#!/usr/bin/python3
"""
here to see the final numeber code
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    new_text = text.replace("_", " ")
    return "C %s" % new_text


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python1(text="is cool"):
    new_text = text.replace("_", " ")
    return "Python %s" % new_text

"""
   try to do here same thing to get
"""
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number1(n):
    print(n)
    return render_template("5-number.html", n=n)


if __name__ == "main":
    app.run(host="0.0.0.0", port=5000)
