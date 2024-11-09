import requests
import time

try:
    f = open("key.txt", "r")
    key = f.read()
    f.close()
except Exception:
    print(Exception)

test = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": key
}

response = requests.get(test, headers=headers)
print(response.status_code)