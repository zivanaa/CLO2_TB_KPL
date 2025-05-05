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
    menu = {
        "1": {"desc": "USD to EUR", "from": "USD", "to": "EUR"},
        "2": {"desc": "USD to IDR", "from": "USD", "to": "IDR"},
        "3": {"desc": "USD to JPY", "from": "USD", "to": "JPY"},
        "4": {"desc": "IDR to USD", "from": "IDR", "to": "USD"},
        "5": {"desc": "EUR to USD", "from": "EUR", "to": "USD"},
        "6": {"desc": "Show all from USD", "from": "USD", "to": None},
        "0": {"desc": "Exit"}
    }

    print("=" * 40)
    print("🌐 Currency Converter Menu (TDC)")
    print("=" * 40)
    for key, item in menu.items():
        print(f"{key}. {item['desc']}")
    print("=" * 40)

    choice = input("Enter your choice: ")

    if choice not in menu:
        print("❌ Invalid option.")
        return

    if choice == "0":
        print("👋 Goodbye!")
        return

    try:
        amount = float(input("Enter amount: "))
        selected = menu[choice]
        if selected["to"]:
            convert_and_print(amount, selected["from"], selected["to"])
        else:
            all_conversions_and_print(amount, selected["from"])
    except Exception as e:
        print(f"⚠ Error: {e}")

if __name__ == "__main__":
    run()