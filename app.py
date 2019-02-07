from flask import (
    Flask, request, render_template, Blueprint, url_for
)
import datetime

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET', 'POST'])
def home():
    alarm_time = datetime.time(8, 0, 0).isoformat()
    alarm_on = False
    if request.method =='POST':
        update_alarm(request.form['time'], 'on' in request.form)
    return render_template('home.html', time=alarm_time, on=alarm_on)

def update_alarm(time, is_on):
    print(f'set time = {time}')
    print(f'set on = {is_on}')

app.run(port=5005, debug=True)
