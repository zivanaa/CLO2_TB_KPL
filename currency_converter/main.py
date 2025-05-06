# main.py

from converter import convert_currency, is_currency_supported
from config import SUPPORTED_CURRENCIES

def display_supported_currencies():
    print("\n--- Supported Currencies ---")
    for code, country in SUPPORTED_CURRENCIES:
        print(f"{code} - {country}")
    print()

def main():
    print("=== Currency Converter ===")
    display_supported_currencies()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., IDR): ").upper()

    if not is_currency_supported(from_currency) or not is_currency_supported(to_currency):
        print("One of the currencies is not supported.")
        return

    try:
        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except AssertionError as ae:
        print(f"Error: {ae}")
    except Exception as e:
        print(f"Conversion failed: {e}")

if __name__ == "__main__":
    main()
