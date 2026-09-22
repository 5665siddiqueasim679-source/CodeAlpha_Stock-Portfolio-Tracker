# 1. Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400
}

print("Available stocks and prices:", stock_prices)

# 2. Get user input for stock name and quantity
stock_name = input("Enter the stock symbol you want to buy (e.g., AAPL): ").upper()
quantity = int(input("Enter the quantity: "))

# 3. Calculate total investment
if stock_name in stock_prices:
    price_per_share = stock_prices[stock_name]
    total_investment = price_per_share * quantity

    # 4. Display the result
    result_message = f"Stock: {stock_name}\nQuantity: {quantity}\nTotal Investment Value: ${total_investment}"
    print("\n" + result_message)

    # 5. Optionally save the result in a .txt file
    save_choice = input("\nDo you want to save this to a file? (y/n): ").lower()
    if save_choice == 'y':
        with open("portfolio_summary.txt", "w") as file:
            file.write(result_message)
        print("Portfolio saved successfully to 'portfolio_summary.txt'!")
else:
    print("Sorry, that stock is not in our price dictionary.")
