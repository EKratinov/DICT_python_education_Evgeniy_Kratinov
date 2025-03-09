import random


def generate_task(level):
    if level == 1:  # Уровень 1: простые операции
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        correct_answer = eval(f"{a} {operation} {b}")
        task = f"{a} {operation} {b}"
    elif level == 2:  # Уровень 2: возведение в квадрат
        a = random.randint(11, 29)
        correct_answer = a ** 2
        task = f"{a}"
    else:
        return None, None

    return task, correct_answer


def get_user_answer(task, correct_answer):
    while True:
        try:
            user_input = input(f"{task}\n> ")
            user_answer = int(user_input)
            if user_answer == correct_answer:
                print("Right!")
                return True
            else:
                print("Wrong!")
                return False
        except ValueError:
            print("Incorrect format.")


while True:
    try:
        level = int(input(
            "Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> "))
        if level in [1, 2]:
            break
        else:
            print("Invalid level. Please enter 1 or 2.")
    except ValueError:
        print("Incorrect format.")


correct_count = 0
for _ in range(5):
    task, correct_answer = generate_task(level)
    if task is not None and correct_answer is not None:
        if get_user_answer(task, correct_answer):
            correct_count += 1

print(f"Your mark is {correct_count}/5.")


save_result = input("Would you like to save your result to the file? Enter yes or no.\n> ").lower()
if save_result in ["yes", "y"]:
    name = input("What is your name?\n> ")
    level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
    with open("results.txt", "a") as file:
        file.write(f"{name}: {correct_count}/5 in level {level} ({level_description}).\n")
    print('The results are saved in "results.txt".')
