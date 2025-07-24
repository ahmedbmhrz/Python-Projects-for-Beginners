class ATM:
    def __init__(self):
        self.balance = 0
    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return False    # print("\nInvalid, Please enter a positive number")

        self.balance += amount
        return True       # print(f"\nDeposited ${amount}")


    def withdraw(self, amount):
        if amount > self.balance or amount <= 0:
            return False  
            
        self.balance -= amount
        return True
         
def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            print(f"\nYour balance is ${atm.check_balance()}")

        elif choice == "2":
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    if atm.deposit(amount):
                        print(f"\nDeposited ${amount}")
                        break
                    else:
                        print("\nInvalid, Please enter a positive number")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    if amount <= 0:
                        print("\nInvalid, Please enter a positive number")
                        continue
                    elif amount > atm.check_balance():
                        print("you don't have enough money")
                        continue
                    else:
                        atm.withdraw(amount)
                        print(f"\nWithdrew ${amount}")
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            print("\nThank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
        