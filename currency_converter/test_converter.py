# test_converter.py

import unittest
from converter import convert_currency, is_currency_supported

class TestCurrencyConverter(unittest.TestCase):
    def test_valid_conversion(self):
        result = convert_currency(1, "USD", "IDR")
        self.assertTrue(result > 0)

    def test_invalid_amount(self):
        with self.assertRaises(AssertionError):
            convert_currency(0, "USD", "IDR")

    def test_unsupported_currency(self):
        with self.assertRaises(AssertionError):
            convert_currency(10, "XXX", "IDR")
    
    def test_invalid_amount_negative(self):
        with self.assertRaises(AssertionError):
            convert_currency(-100, "USD", "IDR")

    def test_same_currency_conversion(self):
        result = convert_currency(50, "USD", "USD")
        self.assertEqual(result, 50)
    
    def test_large_amount_conversion(self):
        result = convert_currency(1_000_000, "EUR", "JPY")
        self.assertTrue(result > 0)

    def test_is_currency_supported_invalid(self):
        self.assertFalse(is_currency_supported("ABC"))

    def test_is_currency_supported_valid(self):
        self.assertTrue(is_currency_supported("USD"))

if __name__ == '__main__':
    unittest.main()
