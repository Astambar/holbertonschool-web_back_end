#!/usr/bin/env python3
"""
Main module for the Flask application.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """
    Configuration class for the Flask application.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
babel.init_app(app)


@app.route('/')
def index():
    """
    Route handler for the home page.
    Renders the '2-index.html' template with the title and hello message.
    """

    title = "Welcome to Holberton"
    h1 = "Hello world"
    return render_template("2-index.html", title=title, hello=h1)


@babel.localeselector
def get_locale():
    """
    Locale selector function to determine the best language for the user.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    # Runs the Flask application on the local development server
    # accessible at http://0.0.0.0:5000/
    app.run(host='0.0.0.0', port=5000)
