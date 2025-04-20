import requests


def get_exchange_rates(currency_code):
    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    response = requests.get(url)

    if response.status_code == 200:
        exchange_data = response.json()
        if "usd" in exchange_data and "eur" in exchange_data:
            print(f"Exchange rate to USD: {exchange_data['usd']['rate']:.2f}")
            print(f"Exchange rate to EUR: {exchange_data['eur']['rate']:.2f}")
        else:
            print("No exchange rate data for USD or EUR.")
    else:
        print("Failed to retrieve exchange rates.")


currency_code = input("Enter currency code: > ").lower()
get_exchange_rates(currency_code)
