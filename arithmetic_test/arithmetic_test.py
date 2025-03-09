import random


def generate_task():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    operation = random.choice(['+', '-', '*'])
    correct_answer = eval(f"{a} {operation} {b}")
    while True:
        try:
            user_input = input(f"{a} {operation} {b}\n> ")
            user_answer = int(user_input)
            if user_answer == correct_answer:
                print("Right!")
                return True
            else:
                print("Wrong!")
                return False
        except ValueError:
            print("Incorrect format.")


correct_count = 0
for _ in range(5):
    if generate_task():
        correct_count += 1

print(f"Your mark is {correct_count}/5.")
