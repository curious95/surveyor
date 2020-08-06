from flask import Flask, render_template, jsonify, request, redirect, url_for, Response
from sqlalchemy import exc
from jinja2 import Template
from datetime import datetime

from app.configuration import Config

import logging
import traceback
import glob

app = Flask(__name__)
config = Config()

# logging.basicConfig(filename=f"/home/groot/workspace/customer_manager/app/logs/{datetime.today().strftime('%Y-%m-%d')}.log",
#                     level=logging.DEBUG,
#                     format=' %(asctime)s %(levelname)s %(name)s %(threadName)s: %(message)s')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
