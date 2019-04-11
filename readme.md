# "Smart" Alarm Clock

This project is currently a work in progress.

The idea is to have a cron job which slowly turns on a LIFX smart bulb in the morning similar to many "wake up light alarm clocks". The cron job time can be set via a very simple Flask webapp which will be available on local network.


## Requirements
- Python 3.6
- virtualenv (`pip install virtualenv`)


## Setup

Generate LIFX access token in [LIFX settings](https://cloud.lifx.com/settings). Copy the `.env.example` file to `.env` and add the access token.

Initial create virtual env:
- `virtualenv --python=/usr/bin/python3.7 venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

Run the app:
- `python app.py`
- It should now be visible at `localhost:5005`


Background photo by Artem Sapegin on Unsplash