#!/usr/bin/env python3
"""
Main module for the Flask application.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app: Flask = Flask(__name__)
babel: Babel = Babel()

users: dict = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request() -> None:
    """
    Before request handler to set the current user in the global context.
    """
    g.user = get_user()


class Config(object):
    """
    Configuration class for the Flask application.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)


@babel.localeselector
def get_locale() -> str:
    """
    Locale selector function to determine the best language for the user.
    """
    locale: str = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in Config.LANGUAGES:
            return locale

    locale = request.headers.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone() -> str:
    """
    Timezone selector function to determine the best timezone for the user.
    """
    timezone: str = request.args.get("timezone")
    if timezone:
        return timezone

    if g.user:
        timezone = g.user.get("timezone")
        if timezone:
            return timezone

    return request.headers.get("timezone")


@app.route("/", methods=["GET"])
def index() -> str:
    """
    Route handler for the home page.
    Renders the '7-index.html' template.
    """
    return render_template("7-index.html")


def get_user() -> dict:
    """
    Get the current user based on the 'login_as' query parameter.
    """
    user_id: str = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    else:
        return None


if __name__ == "__main__":
    # Runs the Flask application on the local development server
    # accessible at http://0.0.0.0:5000/
    app.run(host="0.0.0.0", port="5000")
