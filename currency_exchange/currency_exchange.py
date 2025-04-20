def convert_currency():
    mycoins = float(input("Please, enter the number of mycoins you have: > "))


    exchange_rate = float(input("Please, enter the exchange rate: > "))


    dollars = round(mycoins * exchange_rate, 2)


    print(f"The total amount of dollars: {dollars}")


convert_currency()
