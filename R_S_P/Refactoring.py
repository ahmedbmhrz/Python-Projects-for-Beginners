import random

choices = ("r", "p", "s")


def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissor r/p/s: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("No, Please enter => r/p/s <= ")


def display_choices(user_choice, computer_choice):
    print(f"you chose {user_choice}")
    print(f"computer chose {computer_choice}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        print("You win")
    else:
        print("You lose")


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        play_again = input("Play again? (Y/N): ").lower()
        if play_again == "y":
            play_game()
        if play_again == "n":
            print("Bye")
            break


play_game()
