import config
import json
import requests      

API_KEY = config.API_KEY
SECRET_KEY = config.API_SECRET_KEY
BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
CLOCK_URL = "{}//v2/clock".format(BASE_URL)
HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers = HEADERS)
    return json.loads(r.content)

def create_order(symbol, qty, side,  type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }

    r = requests.post(ORDERS_URL, json = data, headers = HEADERS)
    return json.loads(r.content)

    def clock():
        r = requests.get(CLOCK_URL, headers = HEADERS)
        return json.loads(r.contents)
    