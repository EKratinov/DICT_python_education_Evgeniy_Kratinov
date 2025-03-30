import random


def get_user_choice():
    choice = input("Enter your choice (rock, scissors, paper): ").lower()
    while choice not in ["rock", "scissors", "paper"]:
        print("Invalid input. Please enter: rock, scissors, or paper.")
        choice = input("Enter your choice: ").lower()
    return choice

def get_computer_winning_choice(user_choice):
    win_choices = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
    return win_choices[user_choice]

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_winning_choice(user_choice)
    print(f"Sorry, but the computer chose {computer_choice}")

if __name__ == "__main__":
    main()