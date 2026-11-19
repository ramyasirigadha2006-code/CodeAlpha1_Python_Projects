
print("Welcome to Stock Portfolio Tracker!")

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140
}

total_investment = 0

print("\nAvailable Stocks:")
for name, price in stocks.items():
    print(name, "=", price)

while True:
    stock_name = input("\nEnter stock name (or done to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))

        investment = stocks[stock_name] * quantity
        total_investment += investment

        print("Stock:", stock_name)
        print("Quantity:", quantity)
        print("Investment:", investment)

    else:
        print("Sorry, stock not available!")

print("\nTotal Investment:", total_investment)
print("Thank you for using Stock Portfolio Tracker!")
