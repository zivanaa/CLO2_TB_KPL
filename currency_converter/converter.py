# converter.py

import requests
from config import BASE_URL, SUPPORTED_CURRENCIES

def is_currency_supported(code):
    return code in SUPPORTED_CURRENCIES

def convert_currency(amount, from_currency, to_currency):
    assert amount > 0, "Amount must be greater than 0"
    assert is_currency_supported(from_currency), "Unsupported source currency"
    assert is_currency_supported(to_currency), "Unsupported target currency"

    url = f"{BASE_URL}/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to retrieve exchange rate")

    data = response.json()
    return data["conversion_result"]

def get_all_conversions(amount, from_currency):
    assert amount > 0, "Amount must be greater than 0"
    assert is_currency_supported(from_currency), "Unsupported source currency"

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to retrieve exchange rates")

    data = response.json()
    conversions = {}
    for to_currency in SUPPORTED_CURRENCIES:
        if to_currency == from_currency:
            continue
        rate = data["conversion_rates"].get(to_currency)
        if rate:
            conversions[to_currency] = round(amount * rate, 2)
    
    return conversions