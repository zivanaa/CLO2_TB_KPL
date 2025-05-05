# app_menu_with_history.py

from converter import convert_currency, is_currency_supported
from currency_history import save_conversion, show_history, get_previous_conversion, calculate_percentage_change

def convert_and_print(amount, from_curr, to_curr):
    result = convert_currency(amount, from_curr, to_curr)
    print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
    save_conversion(amount, from_curr, to_curr, result)

def show_exchange_rate(from_curr, to_curr):
    if not is_currency_supported(from_curr) or not is_currency_supported(to_curr):
        print("❌ Unsupported currency.")
        return
    result = convert_currency(1, from_curr, to_curr)
    print(f"1 {from_curr} = {result:.2f} {to_curr}")

def show_percentage_change(from_curr, to_curr, new_amount):
    previous_conversion = get_previous_conversion(from_curr, to_curr)
    if not previous_conversion:
        print("❌ No previous conversion found for this currency pair.")
        return

    old_value = previous_conversion['result']
    percentage_change = calculate_percentage_change(old_value, new_amount)
    print(f"Percentage change from previous conversion: {percentage_change:.2f}%")

def convert_menu():
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD): ").upper()
    to_curr = input("To currency (e.g., IDR): ").upper()

    if not is_currency_supported(from_curr) or not is_currency_supported(to_curr):
        print("❌ Unsupported currency.")
        return

    convert_and_print(amount, from_curr, to_curr)

def show_exchange_menu():
    from_curr = input("From currency (e.g., USD): ").upper()
    to_curr = input("To currency (e.g., IDR): ").upper()
    show_exchange_rate(from_curr, to_curr)

def percentage_change_menu():
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD): ").upper()
    to_curr = input("To currency (e.g., IDR): ").upper()

    if not is_currency_supported(from_curr) or not is_currency_supported(to_curr):
        print("❌ Unsupported currency.")
        return

    convert_and_print(amount, from_curr, to_curr)
    show_percentage_change(from_curr, to_curr, amount)

def print_menu():
    print("="*40)
    print("🌐 Currency Converter with History & Percentage Change")
    print("="*40)
    print("1. Convert Currency")
    print("2. Show Conversion History")
    print("3. Check Current Exchange Rate")
    print("4. Show Percentage Change in Conversion")
    print("0. Exit")
    print("="*40)

def run():
    menu_actions = {
        "1": convert_menu,
        "2": show_history,
        "3": show_exchange_menu,
        "4": percentage_change_menu
    }

    while True:
        print_menu()
        choice = input("Select an option (0-4): ")

        if choice == "0":
            print("👋 Goodbye!")
            break

        action = menu_actions.get(choice)
        if action:
            try:
                action()
            except ValueError:
                print("❌ Please enter a valid number.")
            except Exception as e:
                print(f"⚠  Error: {e}")
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    run()
