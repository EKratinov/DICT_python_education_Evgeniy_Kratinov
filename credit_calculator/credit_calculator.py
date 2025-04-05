import math

def calculate_loan():
    choice = input(
        "What do you want to calculate?\n"
        "type 'n' for number of monthly payments,\n"
        "type 'a' for annuity monthly payment amount,\n"
        "type 'p' for loan principal:\n> "
    )

    if choice == "n":
        principal = float(input("Enter the loan principal: "))
        payment = float(input("Enter the monthly payment: "))
        annual_interest = float(input("Enter the loan interest: "))
        i = annual_interest / 1200
        n = math.log(payment / (payment - i * principal), 1 + i)
        n_ceil = math.ceil(n)
        years = n_ceil // 12
        months = n_ceil % 12
        duration = []
        if years:
            duration.append(f"{years} year{'s' if years != 1 else ''}")
        if months:
            duration.append(f"{months} month{'s' if months != 1 else ''}")
        print("It will take " + " and ".join(duration) + " to repay the loan!")
    elif choice == "a":
        principal = float(input("Enter the loan principal: "))
        periods = int(input("Enter the number of periods: "))
        annual_interest = float(input("Enter the loan interest: "))
        i = annual_interest / 1200
        x = math.pow(1 + i, periods)
        annuity = math.ceil(principal * (i * x) / (x - 1))
        print(f"Your monthly payment = {annuity}!")
    elif choice == "p":
        annuity = float(input("Enter the annuity payment: "))
        periods = int(input("Enter the number of periods: "))
        annual_interest = float(input("Enter the loan interest: "))
        i = annual_interest / 1200
        x = math.pow(1 + i, periods)
        principal = round(annuity / ((i * x) / (x - 1)))
        print(f"Your loan principal = {principal}!")
    else:
        print("Incorrect parameters")

if __name__ == "__main__":
    calculate_loan()
