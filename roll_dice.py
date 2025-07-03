import random

def roll_dice():
    while True:
        A = input("Roll the dice? (Y/N): ")
        match A:
            case "Y" | "y":
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print("You rolled a", dice1)
                print("You rolled a", dice2)
                if dice1 + dice2 == 12:
                    print("you got a 12!")
            case "N" | "n":
                print("Bye")
                break
            case _:
                print("Invalid, Please enter Y or N")

roll_dice()