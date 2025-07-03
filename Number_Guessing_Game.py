import random


def Number_Gussing_Game():
    number = random.randint(1, 50)
    while True:
        A = input("Guss number bteween 1 and 50:  ")
        match A:
            case "Q" | "q":
                print("Bye")
                break
            case _:
                if int(A) == number:
                    print("you got the number!")
                    break
                elif int(A) > number:
                    print("Too high")
                elif int(A) < number:
                    print("Too low")
                else:
                    print("Invalid, Please enter a number bteween 1 and 50")

Number_Gussing_Game()
