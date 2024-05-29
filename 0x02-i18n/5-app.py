#!/usr/bin/env python3
"""
Task 3: Parametrize templates
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    configure available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    returns a user dictionary or None
    """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """
    use get_user to find a user if any
    """
    g.user = get_user()


@app.route('/')
def hello_world():
    """
    outputs “Hello World”
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
