import math


principal = int(input("Enter the loan principal: "))


option = input(
    "What do you want to calculate?\ntype 'm' - for number of monthly payments,\ntype 'p' - for the monthly payment:\n> ")

if option == "m":
    payment = int(input("Enter the monthly payment: "))
    months = math.ceil(principal / payment)
    print(f"It will take {months} months to repay the loan")

elif option == "p":
    months = int(input("Enter the number of months: "))
    payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * payment

    if last_payment != payment:
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
    else:
        print(f"Your monthly payment = {payment}.")
