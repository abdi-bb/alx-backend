#!/usr/bin/env python3
'''
Module: '2-app'
Basic Flask App
'''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    '''Class Config'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def welcome():
    '''Flask App returning html page'''
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    '''Determines best match from supported langs'''
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(debug=True)
