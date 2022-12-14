import os, glob

from flask import (Flask, render_template, request, redirect, url_for)

import time as tm


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


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if request.form['submit_button'] == "Start":
            print("Start")
            
        return redirect(url_for('workload'))
    else:
        return render_template('index.html')

    
@app.route('/workload', methods=['GET', 'POST'])
def workload():

    if request.method == 'POST':
        
        print(request.form)
        if request.form['submit_button'] == "Stop":
             print("Stop")
             return render_template('index.html')
             
        if request.form['submit_button'] == "1":
             print("1")
             save_csv(1)
        elif request.form['submit_button'] == "2":
             print("2")
             save_csv(2)
        elif request.form['submit_button'] == "3":
             print("3")
             save_csv(3)
        elif request.form['submit_button'] == "4":
             print("4")
             save_csv(4)
        elif request.form['submit_button'] == "5":
             print("5")
             save_csv(5)
        elif request.form['submit_button'] == "6":
             print("6")
             save_csv(6)
        elif request.form['submit_button'] == "7":
             print("7")
             save_csv(7)
        elif request.form['submit_button'] == "8":
             print("8")
             save_csv(8)
        elif request.form['submit_button'] == "9":
             print("9")
             save_csv(9)
        elif request.form['submit_button'] == "10":
             print("10")
             save_csv(10)
        else:
            print("else")

        return render_template('workload.html', path_to_audio = url_for('static', filename='short2.wav'))
    else:
        return render_template('workload.html', path_to_audio = url_for('static', filename='short2.wav'))
    
   

def save_csv(score):
    full_filename = "temp.csv";
    isExist = os.path.exists(full_filename)
    if isExist:
        df = pd.read_csv(full_filename, sep=' ',
            #names = ['timestamp', 'score'],
            dtype={'timestamp':int, 'score':int})
    else:
        df = pd.DataFrame();
    ts = round(tm.time());
    df = df.append({'timestamp': ts, 'score': score}, ignore_index=True)
    print(df)
    df.to_csv(full_filename, sep=' ', encoding='utf-8', float_format='%.6f', header=True, index=False)


