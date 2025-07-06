def Currency_Converter():
   
   while True:
     try:
        A = float(input("Enter the amount: "))
        if A <= 0:
         raise ValueError
        break
     except ValueError:
        print("Invalid, Please enter a number")

   currencies = ["USD", "EUR", "CAD"]

   while True:
    original_currency = input("Original currency (USD, EUR, CAD): ")
    if original_currency not in currencies:
        print("Invalid, Please enter USD/EUR/CAD")
    else:
        break

   
   while True:
    target_currency = input("Target the currency (USD, EUR, CAD): ")
    if target_currency not in currencies:
        print("Invalid, Please enter USD/EUR/CAD")
    else:
        break
   
   exchange_rates = {
       'USD': {'EUR': 0.85, 'CAD': 1.28},
       'EUR': {'USD': 1.17, 'CAD': 1.55},
       'CAD': {'USD': 0.78, 'EUR': 0.67}
   }

   converted_amount = A * exchange_rates[original_currency][target_currency]

   print(f"{A} {original_currency} is equal to {converted_amount:.2f} {target_currency}")





    # print("enter the amount of money you want to convert")
    # A = input("Enter the amount: ")
    # print("enter the original currency USD/EUR/CAD")
    # X = input("Enter the currency: ")
    # print("enter the currency you want to convert to USD/EUR/CAD")
    # Y = input("Enter the currency: ")
    # match X:
    #     case "USD":
    #         if Y == "EUR":
    #             print("you got", float(A) * 0.85, "EUR")
    #         elif Y == "CAD":
    #             print("you got", float(A) * 1.28, "CAD")
    #         else:
    #             print("Invalid, Please enter USD/EUR/CAD")
    #     case "EUR":
    #         if Y == "USD":
    #             print("you got", float(A) * 1.17, "USD")
    #         elif Y == "CAD":
    #             print("you got", float(A) * 1.55, "CAD")
    #         else:
    #             print("Invalid, Please enter USD/EUR/CAD")
    #     case "CAD":
    #         if Y == "USD":
    #             print("you got", float(A) * 0.78, "USD")
    #         elif Y == "EUR":
    #             print("you got", float(A) * 0.67, "EUR")
    #         else:
    #             print("Invalid, Please enter USD/EUR/CAD")
    #     case _:
    #         print("Invalid, Please enter USD/EUR/CAD")


Currency_Converter()
