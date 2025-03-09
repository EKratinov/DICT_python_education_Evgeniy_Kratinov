import random


a = random.randint(2, 9)
b = random.randint(2, 9)
operation = random.choice(['+', '-', '*'])


print(f"{a} {operation} {b}")


try:
    user_answer = int(input("> "))
    correct_answer = eval(f"{a} {operation} {b}")
    if user_answer == correct_answer:
        print("Right!")
    else:
        print("Wrong!")
except ValueError:
    print("Incorrect format.")
