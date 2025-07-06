def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Invalid, Please enter a number")

def get_currency(label):
    currencies = ["USD", "EUR", "CAD"]
    while True:
        currency = input(f"{label} currency (USD, EUR, CAD): ")
        if currency not in currencies:
            print("Invalid, Please enter USD/EUR/CAD")
        else:
            return currency

def convert(amount, source_currency, target_currency):
    conversion_rates = {
        "USD": {"EUR": 0.85, "CAD": 1.28},
        "EUR": {"USD": 1.17, "CAD": 1.53},
        "CAD": {"USD": 0.78, "EUR": 0.66}
    }

    if source_currency == target_currency:
        return amount
    return amount * conversion_rates[source_currency][target_currency]

def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()

