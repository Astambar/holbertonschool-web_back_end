#!/usr/bin/env python3
"""
Main module for the Flask application.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configuration class for the Flask application.
    """

    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@app.route("/", methods=["GET"])
def index():
    """
    Route handler for the home page.
    Renders the '1-index.html' template.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    # Runs the Flask application on the local development server
    # accessible at http://0.0.0.0:5000/
    app.run(host="0.0.0.0", port="5000")
