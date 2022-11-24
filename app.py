from config import (DEBUG, PORT, HOST)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

#if __name__ == '__main__':
#    app.run(debug=DEBUG, host=HOST, port=PORT)

'''
from flask import (Flask, render_template, request, redirect, url_for)

from config import (DEBUG, PORT, HOST)
from config import *

import os, glob


from datetime import datetime, time, timedelta
import pytz

import pandas as pd
import numpy as np

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, os.path.join('data', 'output'))


app = Flask(__name__)


app.config.from_object('config')

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

date = 0


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index.html')


#def save_csv(df):

#    df.to_csv(full_filename, sep=' ', encoding='utf-8', float_format='%.6f', header=True, index=False)


#if __name__ == '__main__':
#    app.run(debug=DEBUG, host=HOST, port=PORT)
'''