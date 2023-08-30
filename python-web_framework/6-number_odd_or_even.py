#!/usr/bin/python3
'''
   so we install the flask pakage
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_ctext(text):
    text = text.replace('', ' ')
    return 'C {}'.format(text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_pythontext(text):
    text = text.replace('', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even_template/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
        if n % 2 == 0:
            n = f'Number: {n} is even'
        else:
            n = f'Number: {n} is odd'
        return render_template('6-number_odd_or_even.html', n=n)
'''
   so we install the flask pakage
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)