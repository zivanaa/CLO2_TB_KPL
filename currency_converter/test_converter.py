# test_converter.py

import unittest
from converter import convert_currency

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

if __name__ == '__main__':
    unittest.main()
