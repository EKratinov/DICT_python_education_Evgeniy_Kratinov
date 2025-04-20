import requests

cache = {}


def get_exchange_rate(base_currency, target_currency):
    if not target_currency.isalpha() or len(target_currency) != 3:
        print("Invalid currency code. Please enter a three-letter currency code.")
        return None

    if target_currency in cache:
        print("Checking the cache...")
        print("It is in the cache!")
        return cache[target_currency]

    print("Checking the cache...")
    print("Sorry, but it is not in the cache!")
    print(f"Fetching exchange rate for {target_currency}...")

    url = f"http://www.floatrates.com/daily/{base_currency}.json"
    response = requests.get(url)

    if response.status_code == 200:
        exchange_data = response.json()
        if target_currency in exchange_data:
            rate = exchange_data[target_currency]["rate"]
            cache[target_currency] = rate
            return rate
        else:
            print(f"Exchange rate for {target_currency} is not available.")
    else:
        print("Failed to retrieve exchange rates.")

    return None


def convert_currency():
    base_currency = input("Enter the currency you have: > ").lower()

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
