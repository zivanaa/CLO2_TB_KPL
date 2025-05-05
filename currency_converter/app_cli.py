# app_cli.py (Versi Benar)

from converter import convert_currency, get_all_conversions, is_currency_supported

def convert_and_print(amount, from_curr, to_curr):
    result = convert_currency(amount, from_curr, to_curr)
    print(f"{amount} {from_curr} = {result:.2f} {to_curr}")


def all_conversions_and_print(amount, from_curr):
    results = get_all_conversions(amount, from_curr)
    for k, v in results.items():
        print(f"{amount} {from_curr} = {v} {k}")

def run():
    print("===================================")
    print("      Currency Converter Menu      ")
    print("===================================")
    print("1. Convert USD to EUR")
    print("2. Convert USD to IDR")
    print("3. Convert USD to JPY")
    print("4. Convert IDR to USD")
    print("5. Convert EUR to USD")
    print("6. Show all conversions from USD")
    print("0. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            amount = float(input("Enter amount: "))
            result = convert_currency(amount, "USD", "EUR")
            print(f"{amount} USD = {result:.2f} EUR")
        elif choice == "2":
            amount = float(input("Enter amount: "))
            result = convert_currency(amount, "USD", "IDR")
            print(f"{amount} USD = {result:.2f} IDR")
        elif choice == "3":
            amount = float(input("Enter amount: "))
            result = convert_currency(amount, "USD", "JPY")
            print(f"{amount} USD = {result:.2f} JPY")
        elif choice == "4":
            amount = float(input("Enter amount: "))
            result = convert_currency(amount, "IDR", "USD")
            print(f"{amount} IDR = {result:.2f} USD")
        elif choice == "5":
            amount = float(input("Enter amount: "))
            result = convert_currency(amount, "EUR", "USD")
            print(f"{amount} EUR = {result:.2f} USD")
        elif choice == "6":
            amount = float(input("Enter amount: "))
            results = get_all_conversions(amount, "USD")
            for k, v in results.items():
                print(f"{amount} USD = {v} {k}")
        elif choice == "0":
            print("Goodbye!")
        else:
            print("Invalid input.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()