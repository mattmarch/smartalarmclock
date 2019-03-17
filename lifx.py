import os
import time
import dotenv
import requests

dotenv.load_dotenv()

API_TOKEN = os.getenv('LIFX_KEY')
API_URL = 'https://api.lifx.com/v1'

headers = {
    "Authorization": "Bearer %s" % API_TOKEN,
}


def list_lights():
    response = requests.get(f'{API_URL}/lights/all', headers=headers)
    return response


def set_lights(brightness):
    payload = {'power': 'on', 'brightness': brightness}
    response = requests.put(f'{API_URL}/lights/all/state', data=payload, headers=headers)
    return response


def ramp_on(time_to_on, time_step=5):
    total_steps = int(time_to_on / time_step)
    brightness = 0
    set_lights(brightness)
    brightness_delta = 1 / total_steps
    for _ in range(total_steps):
        time.sleep(time_step)
        brightness += brightness_delta
        set_lights(brightness)


if __name__ == '__main__':
    ramp_on(30)
