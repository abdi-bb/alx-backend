#!/usr/bin/env python3
'''
Module: '4-app'
Basic Flask App
'''

from typing import Dict, Union
from flask import Flask, render_template, request
from flask_babel import Babel, _, gettext

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
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    '''Determines best match from supported langs'''
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in Config.LANGUAGES:
        # If the requested locale is supported, use it
        return requested_locale
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(debug=True)
