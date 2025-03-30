import random


def get_user_choice():
    choice = input("Enter your choice (rock, scissors, paper): ").lower()
    while choice not in ["rock", "scissors", "paper"]:
        print("Invalid input. Please enter: rock, scissors, or paper.")
        choice = input("Enter your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "scissors", "paper"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "Well done. The computer chose " + computer_choice + " and failed"
    else:
        return "Sorry, but the computer chose " + computer_choice

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()
