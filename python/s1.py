# Exchange Rate API
# Get your Free API: https://currencyapi.com/docs

import requests as req

# This KEY is dead. Generate a new one!
api_key = 'cur_live_aK34mQHiXdsY4iHXBugHrm8sHwybWQg6Prc5S4Xx'

api_url = 'https://api.currencyapi.com/v3/latest?apikey='

result = req.get(api_url + api_key)

data = result.json()["data"]

for currency in data:
    print(currency, " : ", data[currency]["value"])
