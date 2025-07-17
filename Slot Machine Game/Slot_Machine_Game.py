import random

def get_starting_balance():
    while True:
        try:
            balance = int(input("Enter your balance: "))
            if balance <= 0:
                print("Invalid, Please enter a positive number")
            else:
                return balance 
        except ValueError:
            print("Invalid, Please enter a number")


def get_bet_amount(balance):
    while True:
        try:
            bet = int(input("Enter your bet: "))
            if bet > balance or bet <= 0:
                print(f"Invalid, Please bet between 1 and {balance}")
            else:
                return bet
        except ValueError:
            print("Invalid, Please enter a number")

def spin_reels():
    symbols = ["🍒", "🍊", "🍋", "🔔", "💰", "💎"]
    return [random.choice(symbols) for _ in range(3)]

def display_reels(reels):
    print(f"{reels[0]} | {reels[1]} | {reels[2]}")

def calculate_winnings(reels, bet):
    if reels[0] == reels[1] == reels[2]:
        symbol = reels[0]
        if symbol == "💎":
            return bet * 20 
        elif symbol == "💰":
            return bet * 15  
        elif symbol == "🔔":
            return bet * 10  
        else:
            return bet * 5   # Lower payout for fruits
    if reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
        return bet * 2
    return 0

def main():
    balance = get_starting_balance()
    if balance is None: 
        return
        
    print("Welcome to the slot machine game!") 
    print(f"You start with ${balance}")
    
    while balance > 0:
        print(f"\nYour balance is ${balance}")

        bet = get_bet_amount(balance)
        reels = spin_reels()
        print("\nSpinning...")
        display_reels(reels)
        payout = calculate_winnings(reels, bet)

        balance -= bet  
        if payout > 0:
            balance += payout
            print(f"You won ${payout}!")
        else:
            print("Sorry, you didn't win this time.")

        if balance == 0:
            print("Sorry, you are out of money!")
            break
            
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print(f"Thank you for playing! You leave with ${balance}")
            break

if __name__ == "__main__":
    main()