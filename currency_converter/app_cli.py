# app_cli.py (Versi Benar)

from converter import convert_currency, get_all_conversions, is_currency_supported

def flexible_mode():
    while True:
        print("=" * 50)
        print("🌐 Currency Converter - Free Mode")
        print("=" * 50)
        print("1. Convert from one currency to another")
        print("2. Show conversions from one currency to ALL")
        print("0. Back to Main Menu")
        print("=" * 50)

        choice = input("Select an option (0-2): ")

        if choice == "0":
            break
        elif choice == "1":
            try:
                amount = float(input("Enter amount: "))
                from_curr = input("From currency (e.g., USD): ").upper()
                to_curr = input("To currency (e.g., IDR): ").upper()

                if not is_currency_supported(from_curr):
                    print("❌ Unsupported source currency.")
                    continue
                if not is_currency_supported(to_curr):
                    print("❌ Unsupported target currency.")
                    continue

                result = convert_currency(amount, from_curr, to_curr)
                print(f"\n💱 {amount} {from_curr} = {result:.2f} {to_curr}\n")
            except ValueError:
                print("❌ Please enter a valid number.")
            except Exception as e:
                print(f"⚠ Error: {e}")
        elif choice == "2":
            try:
                amount = float(input("Enter amount: "))
                from_curr = input("From currency (e.g., USD): ").upper()

                if not is_currency_supported(from_curr):
                    print("❌ Unsupported source currency.")
                    continue
                results = get_all_conversions(amount, from_curr)
                print(f"\n📊 {amount} {from_curr} to other currencies:")
                print("-" * 40)
                for k, v in results.items():
                    print(f"{k: <5}: {v}")
                print()
            except ValueError:
                print("❌ Please enter a valid number.")
            except Exception as e:
                print(f"⚠ Error: {e}")
        else:
            print("❌ Invalid menu option.")

def fixed_mode():
    while True:
        print("=" * 50)
        print("🌐 Currency Converter - Quick Menu")
        print("=" * 50)
        print("1. USD to EUR")
        print("2. USD to IDR")
        print("3. USD to JPY")
        print("4. IDR to USD")
        print("5. EUR to USD")
        print("6. Show all from IDR")
        print("0. Back to Main Menu")
        print("=" * 50)

        choice = input("Enter your choice: ")
        if choice == "0":
            return

        try:
            amount = float(input("Enter amount: "))
            if choice == "1":
                result = convert_currency(amount, "USD", "EUR")
                print(f"{amount} USD = {result:.2f} EUR")
            elif choice == "2":
                result = convert_currency(amount, "USD", "IDR")
                print(f"{amount} USD = {result:.2f} IDR")
            elif choice == "3":
                result = convert_currency(amount, "USD", "JPY")
                print(f"{amount} USD = {result:.2f} JPY")
            elif choice == "4":
                result = convert_currency(amount, "IDR", "USD")
                print(f"{amount} IDR = {result:.2f} USD")
            elif choice == "5":
                result = convert_currency(amount, "EUR", "USD")
                print(f"{amount} EUR = {result:.2f} USD")
            elif choice == "6":
                results = get_all_conversions(amount, "IDR")
                print(f"\n📊 {amount} IDR to popular currencies:")
                print("-" * 40)
                for k, v in results.items():
                    if k in {"USD", "EUR", "JPY", "IDR"}:
                        print(f"{amount} IDR = {v} {k}")
            else:
                print("❌ Invalid menu option.")
            print()
        except Exception as e:
            print(f"⚠ Error: {e}")

def convert_and_print(amount, from_curr, to_curr):
    result = convert_currency(amount, from_curr, to_curr)
    print(f"{amount} {from_curr} = {result:.2f} {to_curr}")


def all_conversions_and_print(amount, from_curr):
    results = get_all_conversions(amount, from_curr)
    for k, v in results.items():
        print(f"{amount} {from_curr} = {v} {k}")

def run():
    while True:
        print("=" * 50)
        print("🌐 Currency Converter with Menu Mode")
        print("=" * 50)
        print("1. Flexible Mode (input currencies manually)")
        print("2. Quick Menu Mode (frequently exchanged currencies)")
        print("0. Exit")
        print("=" * 50)

        choice = input("Select an option (0-2): ")
        if choice == "0":
            print("👋 Goodbye!")
            break
        elif choice == "1":
            flexible_mode()
        elif choice == "2":
            fixed_mode()
        else:
            print("❌ Invalid menu option.")

if __name__ == "__main__":
    run()