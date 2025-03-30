import random

def get_computer_choice():
    return random.choice(["rock", "scissors", "paper"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"There is a draw ({computer_choice})"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return f"Well done. The computer chose {computer_choice} and failed"
    else:
        return f"Sorry, but the computer chose {computer_choice}"

def main():
    while True:
        user_choice = input("Enter your choice (rock, scissors, paper or exit): ").lower()
        if user_choice == "exit":
            print("Bye!")
            break
        elif user_choice in ["rock", "scissors", "paper"]:
            computer_choice = get_computer_choice()
            print(determine_winner(user_choice, computer_choice))
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
