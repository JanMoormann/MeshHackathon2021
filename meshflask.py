import flask
import logging
import os
from dotenv import load_dotenv
from flask import (Flask, jsonify, make_response, redirect,request, render_template, url_for, Response, stream_with_context)


load_dotenv()
app = Flask(__name__)


@app.before_first_request
def before_first_request():
    log_level = logging.INFO
    app.logger.setLevel(log_level)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return "post received - @home"

    elif request.method == 'GET':
        return "get received - @home"


if __name__ == "__main__":
    app.logger.info("logging initialized")
    app.run(debug=False, host='127.0.0.1', port='8080')
