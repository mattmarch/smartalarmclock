import os
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

if __name__ == '__main__':
    print(set_lights(1).text)
