# converter.py

import requests # type: ignore
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
