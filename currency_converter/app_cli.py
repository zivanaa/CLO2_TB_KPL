# app_cli_bad.py (Versi tidak efisien)

from converter import convert_currency, get_all_conversions, is_currency_supported

def run():
    print("===================================")
    print("      Currency Converter Menu      ")
    print("===================================")
    print("1. Convert USD to IDR")
    print("2. Show all conversions from USD")
    print("0. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            amount = float(input("Enter amount: "))
            result = convert_currency(amount, "USD", "IDR")
            print(f"{amount} USD = {result:.2f} IDR")
        elif choice == "2":
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