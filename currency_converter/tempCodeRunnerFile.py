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
    import datetime

    currency_data = load_currency_data()
    currency_history = load_currency_history()

    if not currency_history:
        print("No historical data available.")
        return

    print("\nHourly Currency Exchange Rate Changes (Last 24 Hours):")
    now = datetime.datetime.now()
    last_24_hours = now - datetime.timedelta(hours=24)

    # Ambil data dengan timestamp dalam 24 jam terakhir (bukan hanya berdasarkan tanggal)
    hourly_changes = [
        (timestamp, rates) for timestamp, rates in currency_history.items()
        if last_24_hours <= datetime.datetime.fromisoformat(timestamp) <= now
    ]

    if not hourly_changes:
        print("No data found in the last 24 hours.")
        return

    # Urutkan dan siapkan untuk ditampilkan
    hourly_changes.sort(key=lambda x: x[0])
    rows = [(timestamp, *[f"{rate:.4f}" for rate in rates.values()]) for timestamp, rates in hourly_changes]
    headers = ["Timestamp"] + list(next(iter(hourly_changes))[1].keys())

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
