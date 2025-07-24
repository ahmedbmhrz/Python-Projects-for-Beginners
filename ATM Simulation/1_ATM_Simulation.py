class ATM:
    def __init__(self):
        self.balance = 0
    def check_balance(self):
        print(f"\nYour balance is ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited ${amount}")
        else:
            print("\nInvalid, Please enter a positive number")

    def withdraw(self, amount):
        if amount > self.balance:
            print("you don't have enough money")

        elif amount <= 0:
            print("\nInvalid, Please enter a positive number")
        else:
            self.balance -= amount
            print(f"\nWithdrew ${amount}")
         
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
            atm.check_balance()
        elif choice == "2":
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    atm.deposit(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    atm.withdraw(amount)
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
        