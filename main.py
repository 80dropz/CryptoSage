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
    with open("key.key", "r") as f:
        key = f.read()
except:
    print("Error: config.txt or key.key not found")
    input(" ")
    exit()


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