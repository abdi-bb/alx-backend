#!/usr/bin/env python3
'''
Module: '1-app'
Basic Flask App
'''

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''Default lang'''
    return 'en'


@babel.timezoneselector
def get_timezone():
    '''Default tz'''
    return 'UTC'


@app.route('/')
def welcome():
    '''Flask App returning html page'''
    return render_template('1-index.html')


class Config():
    '''Class Config'''
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)


if __name__ == '__main__':
    app.run(debug=True)
