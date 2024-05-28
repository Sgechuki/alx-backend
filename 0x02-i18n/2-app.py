#!/usr/bin/env python3
"""
Task 2: Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    configure available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def hello_world():
    """
    outputs “Hello World”
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
