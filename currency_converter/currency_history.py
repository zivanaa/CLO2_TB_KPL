# currency_history.py

import datetime

history = []

def save_conversion(amount, from_currency, to_currency, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({
        "amount": amount,
        "from": from_currency,
        "to": to_currency,
        "result": result,
        "timestamp": timestamp
    })

def show_history():
    if not history:
        print("No conversion history yet.")
        return
    print("\nConversion History:")
    print("="*40)
    for entry in history:
        print(f"{entry['amount']} {entry['from']} = {entry['result']} {entry['to']} (at {entry['timestamp']})")
    print("="*40)

def get_previous_conversion(from_currency, to_currency):
    # Mengambil konversi terakhir yang sesuai
    for entry in reversed(history):
        if entry['from'] == from_currency and entry['to'] == to_currency:
            return entry
    return None

def calculate_percentage_change(old_value, new_value):
    if old_value == 0:
        return 0.0
    return ((new_value - old_value) / old_value) * 100
