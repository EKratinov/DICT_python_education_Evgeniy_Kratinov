import random

def get_computer_choice(options):
    return random.choice(options)


def determine_winner(user_choice, computer_choice, options):
    if user_choice == computer_choice:
        return f"There is a draw ({computer_choice})", 50
    else:
        half = len(options) // 2
        index = options.index(user_choice)
        winning_options = options[index + 1: index + 1 + half]

        if computer_choice in winning_options:
            return f"Sorry, but the computer chose {computer_choice}", 0
        else:
            return f"Well done. The computer chose {computer_choice} and failed", 100


def read_rating(user_name):
    try:
        with open("rating.txt", "r") as file:
            for line in file:
                name, score = line.split()
                if name == user_name:
                    return int(score)
    except FileNotFoundError:
        with open("rating.txt", "w") as file:
            pass
    return 0


def write_rating(user_name, rating):
    try:
        with open("rating.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    updated = False
    with open("rating.txt", "w") as file:
        for line in lines:
            name, score = line.split()
            if name == user_name:
                file.write(f"{name} {rating}\n")
                updated = True
            else:
                file.write(line)
        if not updated:
            file.write(f"{user_name} {rating}\n")


def main():
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

    rating = read_rating(user_name)

    options_input = input("Enter the options separated by commas (or press Enter for default): ").strip()
    if options_input:
        options = options_input.split(",")
    else:
        options = ["rock", "scissors", "paper"]

    print("Okay, let's start")


    while True:
        user_choice = input("> ")
        if user_choice == "!exit":
            print("Bye!")
            write_rating(user_name, rating)
            break
        elif user_choice == "!rating":
            print(f"Your rating: {rating}")
        elif user_choice in options:
            computer_choice = get_computer_choice(options)
            result, points = determine_winner(user_choice, computer_choice, options)
            print(result)
            rating += points
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
