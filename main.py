import customtkinter
from customtkinter import filedialog
import webbrowser
import json
import requests
import time
from elevate import elevate

#You can only send a MAX of 13 calls per day or 1 every 2 hours to stay on the free version
#will add adding more api's so you can send more calls if you want just would need diffrent accounts buts its allg
try:
    with open("config.txt", "r") as f:
        settings = f.readlines() 
        coins = settings[0]
    with open("key.key", "r") as f:
        key = f.read()
except:
    print("Error: config.txt or key.key not found")
    input(" ")
    exit()
print(coins)


#this will calculate the average price of 7 days for the given coin
avgpricecall = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": key
}
response = requests.get(avgpricecall, headers=headers)
data = response.json()
for crypto in data['data']:
    if crypto['symbol'] == 'BTC':  # Checking if the cryptocurrency is Bitcoin
        BTCurrentPrice = crypto['quote']['USD']['price']
        percent_change_7d = crypto['quote']['USD']['percent_change_7d']
        Oldbtc = BTCurrentPrice / (1+ (percent_change_7d/100))
        averageBTCprice = (BTCurrentPrice + Oldbtc) / 2
        print(averageBTCprice)



while True:
    test = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": key
    }
    response = requests.get(test, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=16))
    else:
        print(f"Error: {response.status_code}")
    time.sleep(3600)