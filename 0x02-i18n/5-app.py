#!/usr/bin/env python3
'''
Module: '5-app'
Basic Flask App
'''

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, gettext

app = Flask(__name__)
babel = Babel(app)


class Config():
    '''Class Config'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """

    g.user = get_user()


@app.route('/')
def welcome():
    '''Flask App returning html page'''
    return render_template('5-index.html')


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
