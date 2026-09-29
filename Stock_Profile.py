def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOGL": 140.0,
        "MSFT": 400.0,
        "AMZN": 175.0
    }

    portfolio = {}
    total_investment = 0.0

    print("=" * 40)
    print("      S T O C K   T R A C K E R      ")
    print("=" * 40)
    print("Available Stocks & Prices:")
    for symbol, price in stock_prices.items():
        print(f"  {symbol}: ${price:.2f}")
    print("-" * 40)

    while True:
        symbol = input("\nEnter stock symbol (or 'done') --> ").strip().upper()
        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print(">> Invalid symbol. Please select from the list. <<")
            continue

        try:
            quantity = int(input(f"Enter quantity for {symbol} --> "))
            if quantity <= 0:
                print(">> Quantity must be greater than zero. <<")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
            print(f">> Added {quantity} shares of {symbol} <<")
        except ValueError:
            print(">> Invalid number format. Enter an integer. <<")

    if not portfolio:
        print("\n>> No stocks added. Exiting... <<")
        return

    print("\n" + "=" * 40)
    print("         PORTFOLIO SUMMARY         ")
    print("=" * 40)

    summary_lines = ["=== Portfolio Summary ===\n"]
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        value = qty * price
        total_investment += value
        line = f"{symbol}: {qty} shares @ ${price:.2f} = ${value:.2f}"
        print(line)
        summary_lines.append(line + "\n")

    print("-" * 40)
    total_str = f"Total Investment Value: ${total_investment:.2f}"
    print(total_str)
    print("=" * 40)
    summary_lines.append("\n" + total_str + "\n")

    save = input("\nSave summary to 'portfolio.txt'? (y/n) --> ").strip().lower()
    if save == 'y':
        with open("portfolio.txt", "w") as file:
            file.writelines(summary_lines)
        print("\n>> Summary saved to 'portfolio.txt'. <<")

if __name__ == "__main__":
    stock_portfolio_tracker()
