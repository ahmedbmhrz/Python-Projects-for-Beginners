class ATM:
    def __init__(self):
        self.balance = 0
    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
           raise ValueError("\nInvalid, Please enter a positive number")
        self.balance += amount


    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("\nInvalid, Please enter a positive number")
        if amount > self.balance:
            raise ValueError("you don't have enough money")
            
        self.balance -= amount
         
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
                    print(f"\nDeposited ${amount}")
                    break
                except ValueError as e:
                    print(e)
        elif choice == "3":
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    atm.withdraw(amount)
                    print(f"\nWithdrew ${amount}")
                    break
                except ValueError as e:
                    print(e)
        elif choice == "4":
            print("\nThank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
        