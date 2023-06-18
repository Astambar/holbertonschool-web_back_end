#!/usr/bin/env python3
"""
Main module for the Flask application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Route handler for the home page.
    Renders the '0-index.html' template.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    # Runs the Flask application on the local development server
    # accessible at http://0.0.0.0:5000/
    app.run(host="0.0.0.0", port="5000")
