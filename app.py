import os
import sys

from flask import (Flask, render_template, request, redirect, url_for, session)

from datetime import datetime
from datetime import timedelta
import pytz

import pandas as pd

import forms

#TEST = True
TEST = False

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, os.path.join('data', 'output'))

app = Flask(__name__)
app.secret_key = 'qwerwcwdqgfqwefq'

app.config.from_object('config')

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

date = 0


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    
    form = forms.ExperimentForm(request.form)
    
    if request.method == 'POST' and form.validate():
    
    #if request.method == 'POST':
        if request.form['submit_button'] == "Submit":
            
            session['experiment_name'] = request.form['exname']
            session['pilot_name'] = request.form['piname']
            
            try:
                time_interval_min = int(request.form['timeint'])
                session['time_interval_sec'] = time_interval_min * 60
            except ValueError:
                session['time_interval_sec'] = 300
            
            if TEST:
                session['time_interval_sec'] = 5
            
            return redirect(url_for('start'))
    else:

        return render_template('index.html', form=form)


@app.route('/start', methods=['GET', 'POST'])
def start():

    if request.method == 'POST':
        if request.form['submit_button'] == "Start":

            #addr = request.remote_addr.replace(".", "_" )

            start_local_datetime = datetime.now()

            start_swedish_datetime = start_local_datetime.astimezone(pytz.timezone("Europe/Stockholm"))

            start_datetime_str = start_swedish_datetime.strftime("%y%m%d_%H%M%S")

            #session['filename'] = addr + '_' + start_datetime_str + '.csv'
            session['filename'] = session['experiment_name'] + '_' + session['pilot_name'] + '_' + start_datetime_str + '.csv'

            session['start_timestamp'] = start_swedish_datetime.timestamp()
            print("start, timestamp: ", session['start_timestamp'])

        return redirect(url_for('workload'))
    else:
        if 'time_interval_sec' in session:
            return render_template('start_page.html')
        else:
            return redirect(url_for('index'))


@app.route('/workload', methods=['GET', 'POST'])
def workload():

    if request.method == 'POST':

        print(request.form)
        if request.form['submit_button'] == "Stop":
             print("Stop")
             return redirect(url_for('index'))

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
        elif request.form['submit_button'] == "0":
             print("0")
             save_csv(0)
        else:
            print("else")

        print("workload post, time_interval_sec: ", session['time_interval_sec'])
        return render_template('workload.html', path_to_audio = url_for('static', filename='notification.wav'), time_int = session['time_interval_sec'])
    else:
        if 'time_interval_sec' in session:
            print("workload get, time_interval_sec: ", session['time_interval_sec'])
            return render_template('workload.html', path_to_audio = url_for('static', filename='notification.wav'), time_int = session['time_interval_sec'])
        else:
            return redirect(url_for('index'))



def save_csv(score):

    timeIntervalInSeconds = session['time_interval_sec']

    if 'filename' in session:

        filename = session['filename']
        start_timestamp = session['start_timestamp']
        
        print("save, timestamp: ", start_timestamp)

        utc_start_datetime = datetime.utcfromtimestamp(start_timestamp)

        start_swedish_datetime = pytz.utc.localize(utc_start_datetime).astimezone(pytz.timezone("Europe/Stockholm"))

        # I assume no records at midnight (Stockholm time)
        record_date_str = start_swedish_datetime.strftime("%y%m%d")

        print("save_csv", file=sys.stderr, flush=True)
        print(filename, file=sys.stderr, flush=True)

        isExist = os.path.exists(filename)
        if isExist:
            df = pd.read_csv(filename, sep=' ',
                             #names = ['date', 'time', 'timestamp', 'score'],
                             dtype={'date': int, 'time': int, 'timestamp':int, 'score':int})
            record_datetime = start_swedish_datetime + timedelta(seconds=timeIntervalInSeconds * len(df))
            record_time_str = record_datetime.strftime("%H%M%S")
            record_timestamp = int(record_datetime.timestamp())

        else:
            df = pd.DataFrame();
            record_time_str = start_swedish_datetime.strftime("%H%M%S")
            record_timestamp = int(start_swedish_datetime.timestamp())
        
        df = pd.concat([df, pd.DataFrame({'date': [record_date_str],
                                'time': [record_time_str],
                                'timestamp': [str(record_timestamp)],
                                'score': [str(score)]
                                })])
                
        #print(df)
        df.to_csv(filename, sep=' ', encoding='utf-8', float_format='%.6f', header=True, index=False)
    
