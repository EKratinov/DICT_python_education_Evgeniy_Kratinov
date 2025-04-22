import requests
import json
import time
import os

CACHE_FILE = "cache.json"
CACHE_TTL = 300  # 5 минут (в секундах)


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(cache, file, indent=4)


cache = load_cache()


def refresh_cache(base_currency):

    current_time = time.time()

    if "last_updated" in cache and current_time - cache["last_updated"] < CACHE_TTL:
        return

    print("Refreshing cache...")
    url = f"http://www.floatrates.com/daily/{base_currency}.json"
    response = requests.get(url)

    if response.status_code == 200:
        cache_data = response.json()
        cache.clear()
        cache["last_updated"] = current_time

        for currency, data in cache_data.items():
            cache[currency] = {"rate": data["rate"], "timestamp": current_time}

        save_cache(cache)


def get_exchange_rate(base_currency, target_currency):
    refresh_cache(base_currency)

    if target_currency in cache:
        print("Checking the cache...")
        print("It is in the cache!")
        return cache[target_currency]["rate"]

    print("Exchange rate not available.")
    return None


def convert_currency():
    base_currency = input("Enter the currency you have: > ").lower()
    refresh_cache(base_currency)

    while True:
        target_currency = input("Enter the currency to convert to (or press Enter to exit): > ").lower()
        if not target_currency:
            break

        amount = input(f"Enter the amount of {base_currency} to convert: > ")

        if not amount.replace(".", "", 1).isdigit():
            print("Invalid amount. Please enter a numeric value.")
            continue

        amount = float(amount)
        rate = get_exchange_rate(base_currency, target_currency)

        if rate:
            converted_amount = round(amount * rate, 2)
            print(f"You received {converted_amount} {target_currency}.")


convert_currency()
