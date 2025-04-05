import sys
import math

def parse_args():
    args = {}
    for arg in sys.argv[1:]:
        if not arg.startswith("--") or "=" not in arg:
            print("Incorrect parameters")
            sys.exit()
        key, value = arg.lstrip("--").split("=", 1)
        args[key] = value
    return args

def process_args():
    args = parse_args()
    if "type" not in args or "interest" not in args:
        print("Incorrect parameters")
        return
    calc_type = args["type"]
    if calc_type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        return
    for param in ["principal", "payment", "periods", "interest"]:
        if param in args:
            try:
                if float(args[param]) < 0:
                    print("Incorrect parameters")
                    return
            except:
                print("Incorrect parameters")
                return
    if calc_type == "diff":
        if "payment" in args or "principal" not in args or "periods" not in args:
            print("Incorrect parameters")
            return
        principal = float(args["principal"])
        periods = int(float(args["periods"]))
        interest = float(args["interest"])
        i = interest / 1200
        total = 0
        for m in range(1, periods + 1):
            d = math.ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
            total += d
            print(f"Month {m}: payment is {d}")
        print(f"Overpayment = {int(total - principal)}")
    elif calc_type == "annuity":
        provided = {k for k in ["principal", "payment", "periods"] if k in args}
        if len(provided) != 2:
            print("Incorrect parameters")
            return
        interest = float(args["interest"])
        i = interest / 1200
        if "payment" not in args:
            principal = float(args["principal"])
            periods = int(float(args["periods"]))
            x = math.pow(1 + i, periods)
            payment = math.ceil(principal * i * x / (x - 1))
            print(f"Your monthly payment = {payment}!")
            print(f"Overpayment = {int(payment * periods - principal)}")
        elif "principal" not in args:
            payment = float(args["payment"])
            periods = int(float(args["periods"]))
            x = math.pow(1 + i, periods)
            principal = round(payment / (i * x / (x - 1)))
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {int(payment * periods - principal)}")
        elif "periods" not in args:
            principal = float(args["principal"])
            payment = float(args["payment"])
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
            print(f"Overpayment = {int(payment * n_ceil - principal)}")
        else:
            print("Incorrect parameters")

if __name__ == "__main__":
    process_args()
