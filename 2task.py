# Install first: pip install pandas

import csv

stocks = {
    "TCS": 3500,
    "INFY": 1800,
    "RELIANCE": 2900,
    "WIPRO": 550,
    "HDFC": 1700
}

portfolio = {}

print("Stock Portfolio Tracker")
print()

while True:
    print("\n1. Show Stocks")
    print("2. Buy Stock")
    print("3. View Portfolio")
    print("4. Save Portfolio")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Stocks:")
        for name, price in stocks.items():
            print(name, "-", price)

    elif choice == "2":
        name = input("Enter stock name: ").upper()

        if name in stocks:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    if name in portfolio:
                        portfolio[name] += quantity
                    else:
                        portfolio[name] = quantity

                    amount = stocks[name] * quantity
                    print("Investment:", amount)
                else:
                    print("Enter a valid quantity.")

            except ValueError:
                print("Enter a number.")

        else:
            print("Stock not found.")

    elif choice == "3":
        if not portfolio:
            print("Portfolio is empty.")
        else:
            total = 0

            print("\nYour Portfolio:")

            for name, quantity in portfolio.items():
                value = stocks[name] * quantity
                total += value
                print(name, "-", quantity, "shares =", value)

            print("Total Investment:", total)

    elif choice == "4":
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Stock", "Quantity", "Price", "Investment"])

            for name, quantity in portfolio.items():
                value = stocks[name] * quantity
                writer.writerow([name, quantity, stocks[name], value])

        print("Portfolio saved.")

    elif choice == "5":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")