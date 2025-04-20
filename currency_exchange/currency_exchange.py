def convert_multiple_currencies():
    mycoins = float(input("Please, enter the number of mycoins you have: > "))

    exchange_rates = {
        "ARS": 0.82,
        "HNL": 0.17,
        "AUD": 1.9622,
        "MAD": 0.208
    }

    for currency, rate in exchange_rates.items():
        converted_amount = round(mycoins * rate, 2)
        print(f"I will get {converted_amount} {currency} from the sale of {mycoins} mycoins.")

convert_multiple_currencies()
