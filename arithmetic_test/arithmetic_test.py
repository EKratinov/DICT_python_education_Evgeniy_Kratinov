import random

def generate_task(level):
    if level == 1:  # Уровень 1: простые операции
        number1 = random.randint(2, 9)
        number2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        correct_result = eval(f"{number1} {operation} {number2}")
        task_description = f"{number1} {operation} {number2}"
    elif level == 2:  # Уровень 2: возведение в квадрат
        number1 = random.randint(11, 29)
        correct_result = number1 ** 2
        task_description = f"{number1}"
    else:
        return None, None

    return task_description, correct_result

def get_user_answer(task_description, correct_result):
    while True:
        try:
            user_input = input(f"{task_description}\n> ")
            user_result = int(user_input)
            if user_result == correct_result:
                print("Right!")
                return True
            else:
                print("Wrong!")
                return False
        except ValueError:
            print("Incorrect format.")

def get_level():
    while True:
        try:
            level = int(input(
                "Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> "))
            if level in [1, 2]:
                return level
            else:
                print("Invalid level. Please enter 1 or 2.")
        except ValueError:
            print("Incorrect format.")

def play_quiz(level):
    correct_answers = 0
    for _ in range(5):
        task_description, correct_result = generate_task(level)
        if task_description is not None and correct_result is not None:
            if get_user_answer(task_description, correct_result):
                correct_answers += 1
    return correct_answers

def save_results(correct_count, level):
    save_result = input("Would you like to save your result to the file? Enter yes or no.\n> ").lower()
    if save_result in ["yes", "y"]:
        name = input("What is your name?\n> ")
        level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
        with open("results.txt", "a") as file:
            file.write(f"{name}: {correct_count}/5 in level {level} ({level_description}).\n")
        print('The results are saved in "results.txt".')

def main():
    level = get_level()
    correct_count = play_quiz(level)
    print(f"Your mark is {correct_count}/5.")
    save_results(correct_count, level)

if __name__ == "__main__":
    main()
