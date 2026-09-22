# Stock Portfolio Calculator

A simple command-line tool that calculates the total investment value for a stock purchase, using a hardcoded dictionary of stock prices.

## How to Use

1. Run the script:
   ```bash
   python portfolio_calculator.py
   ```
2. Enter a stock symbol from the available list (AAPL, TSLA, GOOGL, MSFT).
3. Enter the quantity of shares you want to buy.
4. The script calculates and displays the total investment value.
5. Optionally, save the summary to `portfolio_summary.txt`.

## Requirements

- Python 3.x (no external dependencies)

## Example

```
Available stocks and prices: {'AAPL': 180, 'TSLA': 250, 'GOOGL': 140, 'MSFT': 400}
Enter the stock symbol you want to buy (e.g., AAPL): aapl
Enter the quantity: 10

Stock: AAPL
Quantity: 10
Total Investment Value: $1800

Do you want to save this to a file? (y/n): y
Portfolio saved successfully to 'portfolio_summary.txt'!
```

## Author

**Asim Siddique** — [@5665siddiqueasim679-source](https://github.com/5665siddiqueasim679-source)

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
