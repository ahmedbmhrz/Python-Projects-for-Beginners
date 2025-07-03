import random

def Rock_Paper_Scissor():
 choices = ("r","p","s")      
 user_choice = input("Reoc,Paper, or scissor r/p/s: ").lower()
 if user_choice not in choices:
    print("Invalid, Please enter r/p/s")

 computer_choice = random.choice(choices)

 print(f'you chose {user_choice}')
 print(f'computer chose {computer_choice}')
 if user_choice == computer_choice:
    print("Tie") 
 elif(
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")):
        print("You win")
 else:
        print("You lose")

 C = input("continue... ,Y/N??").lower()
 if C == "y":
  Rock_Paper_Scissor()
 else:
  print("Bye")

Rock_Paper_Scissor()
