#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Displays Web """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Displays Web """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Displays a letter C followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Displays Python, followed by the value of the text variable,
    with default value of text: is cool """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ The number route """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
