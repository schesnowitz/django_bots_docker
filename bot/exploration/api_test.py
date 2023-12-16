import requests
import pandas as pd
import json


API_KEY = "fb4c44655fe8a67467f67b6094ac3131-f3c5917cdf6b414289e70296954153fe"
ACCOUNT_ID = "101-001-27615226-001"
OANDA_URL = "https://api-fxpractice.oanda.com/v3/"

session = requests.Session()

session.headers.update({
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
})


params = ({
    "count" : 10,
    "granularity" : "H1",
    "price" : "MBA" 
})

url = f"{OANDA_URL}/accounts/{ACCOUNT_ID}/instruments"

response = session.get(url=url, params=None, data=None, headers=None)

response.status_code

json_data = response.json()

# data.keys()
instrument_list = json_data["instruments"]

len(instrument_list)
instrument_list[0].keys()

key_of_interest = ['name', 'type', 'displayName', 'pipLocation', 'displayPrecision', 'tradeUnitsPrecision', 'marginRate']


instruments_dict = {}
for i in instrument_list:
    key = (i["name"])
    instruments_dict[key] = {k: i[k] for k in key_of_interest}
    


with open("bot/data/instruments.json", 'w') as f:
    f.write(json.dumps(instruments_dict, indent=2))


def fetch_candles(currency_pair, count=10, granularity="H1"):
    url = f"{OANDA_URL}/instruments/{currency_pair}/candles"
    params = dict(        
        count = count,
        granularity = granularity,
        price = "MBA" 
    )

     
    response = session.get(url=url, params=params, data=None, headers=None)
    data = response.json()
    # print((data))

    if response.status_code == 200:
        if 'candles' not in data:
            data = []
        else:
            data = data["candles"]
    return response.status_code, data

    

status, candle_data = fetch_candles("EUR_USD", count=1)    

print(status)
print(len(candle_data))
# print((candle_data[0]))