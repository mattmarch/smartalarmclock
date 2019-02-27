from flask import (
    Flask, request, redirect, render_template, Blueprint, url_for
)
import datetime

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def home():
    alarm_time = datetime.time(8, 0, 0).isoformat()
    alarm_on = False
    return render_template('home.html', time=alarm_time, on=alarm_on)

@app.route('/', methods=['POST'])
def update_alarm():
    time = request.form['time']
    is_on = 'on' in request.form    
    print(f'set time = {time}')
    print(f'set on = {is_on}')
    return redirect('/')

if __name__ == '__main__':
    app.run(port=5005, debug=True)
