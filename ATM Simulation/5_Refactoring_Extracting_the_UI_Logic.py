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
         


class ATMController:
    def __init__(self):
        self.atm = ATM()
    

    def get_number(self,prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print("\nInvalid, Please enter a positive number")
    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def check_balance(self):
        balance = self.atm.check_balance()
        print(f"\nYour balance is ${balance}")

    def deposit(self):
        while True:
            try:
                amount = self.get_number("Enter the amount to deposit: ")
                self.atm.deposit(amount)
                print(f"\nDeposited ${amount}")
                break
            except ValueError as e:
                print(e)

    def withdraw(self):
        while True:
            try:
                amount = self.get_number("Enter the amount to withdraw: ")
                self.atm.withdraw(amount)
                print(f"\nWithdrew ${amount}")
                break
            except ValueError as e:
                print(e)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("\nThank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


def main():
    atm = ATMController()
    atm.run()




if __name__ == "__main__":
    main()
        