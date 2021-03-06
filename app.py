from flask import (
    Flask, request, redirect, render_template, Blueprint, url_for
)
import datetime, dateutil.parser
import os, dotenv

import alarm_scheduler
from AlarmState import AlarmState

dotenv.load_dotenv()
FLASK_PORT = os.getenv('FLASK_PORT')
FLASK_HOST = os.getenv('FLASK_HOST')

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def home():
    alarm_state = alarm_scheduler.get_state()
    if alarm_state is None:
        alarm_state = AlarmState.default()
    alarm_time = alarm_state.time.isoformat()
    alarm_on = alarm_state.enabled
    return render_template('home.html', time=alarm_time, on=alarm_on)

@app.route('/', methods=['POST'])
def update_alarm():
    iso_time = request.form['time']
    is_on = 'on' in request.form
    alarm_time = dateutil.parser.parse(iso_time).time()
    alarm_scheduler.update_job(is_on, alarm_time)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(port=FLASK_PORT, host=FLASK_HOST)
