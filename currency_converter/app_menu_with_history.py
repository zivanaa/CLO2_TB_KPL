import datetime
from currency_data import load_currency_data, load_currency_history
from display_utils import print_table

def app_menu():
    while True:
        print("\nCurrency Tracker Menu:")
        print("1. Show Hourly Exchange Rate Change")
        print("2. Show Conversion History")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            show_hourly_change()
        elif choice == '2':
            show_conversion_history()
        elif choice == '3':
            print("Exiting Currency Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def show_hourly_change():
    print("\nHourly Currency Exchange Rate Changes:")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Must be a number.")
        return

    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., IDR): ").upper()

    currency_data = load_currency_data()
    if not currency_data or from_currency not in currency_data or to_currency not in currency_data:
        print("Currency data unavailable or invalid currency code.")
        return

    hourly_changes = list(load_currency_history().items())[-24:]

    print(f"\nHourly Exchange Rate and Conversion from {from_currency} to {to_currency} (Last 24 Hours):")

    headers = ["Time", "Pair", "Rate", "Converted Amount", "Change"]
    rows = []
    previous_rate = None

    for timestamp, rates in hourly_changes:
        if from_currency not in rates or to_currency not in rates:
            continue
        try:
            rate = rates[to_currency] / rates[from_currency]
            converted = rate * amount
            pair = f"{from_currency} to {to_currency}"

            # Hitung perubahan dari sebelumnya (delta)
            if previous_rate is not None:
                change = rate - previous_rate
                change_str = f"{change:+.4f}"
            else:
                change_str = "N/A"

            rows.append([timestamp, pair, f"{rate:.4f}", f"{converted:.2f}", change_str])
            previous_rate = rate
        except Exception:
            continue

    if not rows:
        print("No valid exchange rate data found for the selected currencies.")
        return

    print_table(headers, rows)


def show_conversion_history():
    try:
        with open("conversion_history.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No conversion history found.")
                return
            print("\nConversion History:")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("Conversion history file not found.")

if __name__ == "__main__":
    app_menu()
