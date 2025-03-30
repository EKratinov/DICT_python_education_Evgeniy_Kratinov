import random

def get_computer_choice():
    return random.choice(["rock", "scissors", "paper"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"There is a draw ({computer_choice})", 50
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return f"Well done. The computer chose {computer_choice} and failed", 100
    else:
        return f"Sorry, but the computer chose {computer_choice}", 0

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


    while True:
        user_choice = input("Enter your choice (rock, scissors, paper, !rating, or !exit): ").lower()
        if user_choice == "!exit":
            print("Bye!")
            write_rating(user_name, rating)
            break
        elif user_choice == "!rating":
            print(f"Your rating: {rating}")
        elif user_choice in ["rock", "scissors", "paper"]:
            computer_choice = get_computer_choice()
            result, points = determine_winner(user_choice, computer_choice)
            print(result)
            rating += points
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
