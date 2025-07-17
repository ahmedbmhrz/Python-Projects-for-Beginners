import random

def check_balance(balance):
    try:
        balance = int(balance)
    except ValueError:
        print("Invalid, Please enter a number")
        return False
    if balance < 1:
        print("Invalid, Please enter a number greater than 0")
        return False
    return True

def spin_wheel():
    symbols = ["🍒", "🍊", "🍋", "🔔", "💰", "💎"]
    return random.choice(symbols)

def check_winnings(slot1, slot2, slot3):
    if slot1 == slot2 == slot3:
        if slot1 == "🔔":
            print("You won 3 🔔 = 25") 
            return 100
        elif slot1 == "💰":
            print("You won 3 💰 = 50") 
            return 250
        elif slot1 == "💎":
            print("You won 3 💎 = 100") 
            return 500
        else:
            print(f"You won 3 {slot1} = 5")
            return 5
    return 0

def main():
    balance = input("How much money do you want to put in the machine? ")

    if check_balance(balance):
        balance = int(balance)
        while balance > 0:
            print(f"\nYour balance is ${balance}")
            bet = input("How much do you want to bet? ")
            if not check_balance(bet):
                continue
            bet = int(bet)
            if bet > balance:
                print("Invalid, You don't have enough money")
                continue
            
            balance -= bet
            print("\nSpinning...")
            slot1 = spin_wheel()
            slot2 = spin_wheel()
            slot3 = spin_wheel()
            print(f"\n{slot1} | {slot2} | {slot3}")
            
            winnings = check_winnings(slot1, slot2, slot3)
            if winnings > 0:
                winnings *= bet  
                balance += winnings
                print(f"You won ${winnings}!")
            else:
                print("Sorry, you didn't win this time.")
        print("\nGame over. You're out of money.")

if __name__ == "__main__":
    main()