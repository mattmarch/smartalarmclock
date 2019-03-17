from flask import (
    Flask, request, redirect, render_template, Blueprint, url_for
)
import datetime

import alarm_scheduler
from AlarmState import AlarmState

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
    time = request.form['time']
    is_on = 'on' in request.form
    alarm_time = datetime.time.fromisoformat(time)
    alarm_scheduler.update_job(is_on, alarm_time)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0')
