#!/usr/bin/env python3
"""
Task 0: Basic Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    outputs “Hello World”
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
