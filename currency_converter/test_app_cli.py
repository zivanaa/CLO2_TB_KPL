import unittest
from unittest.mock import patch, MagicMock
import builtins

import app_cli

class TestAppCLI(unittest.TestCase):

    @patch("builtins.print")
    def test_print_menu(self, mock_print):
        title = "Test Menu"
        options = {
            "1": {"desc": "Option One"},
            "2": {"desc": "Option Two"}
        }
        app_cli.print_menu(title, options)
        mock_print.assert_any_call("=" * 50)
        mock_print.assert_any_call(f"🌐 {title}")
        mock_print.assert_any_call("1. Option One")
        mock_print.assert_any_call("2. Option Two")

    @patch("builtins.input", side_effect=["0"])
    @patch("app_cli.print_menu")
    def test_flexible_mode_exit(self, mock_print_menu, mock_input):
        app_cli.flexible_mode()
        mock_input.assert_called_with("Select an option (0-2): ")

    @patch("builtins.input", side_effect=["1", "100", "USD", "EUR", "0"])
    @patch("app_cli.is_currency_supported", return_value=True)
    @patch("app_cli.convert_currency", return_value=150.0)
    @patch("builtins.print")
    def test_flexible_mode_conversion(self, mock_print, mock_convert, mock_support, mock_input):
        app_cli.flexible_mode()
        mock_convert.assert_called_with(100.0, "USD", "EUR")
        mock_print.assert_any_call("\n💱 100.0 USD = 150.00 EUR\n")

    @patch("builtins.input", side_effect=["2", "200", "USD", "0"])
    @patch("app_cli.is_currency_supported", return_value=True)
    @patch("app_cli.get_all_conversions", return_value={"EUR": 180.0, "JPY": 22000.0})
    @patch("builtins.print")
    def test_flexible_mode_all_conversions(self, mock_print, mock_get_all, mock_support, mock_input):
        app_cli.flexible_mode()
        mock_get_all.assert_called_with(200.0, "USD")
        mock_print.assert_any_call("EUR  : 180.0")

    @patch("builtins.input", side_effect=["0"])
    @patch("builtins.print")
    def test_fixed_mode_exit(self, mock_print, mock_input):
        app_cli.fixed_mode()
        mock_input.assert_called_with("Enter your choice: ")

    @patch("builtins.input", side_effect=["1", "100", "0"])
    @patch("app_cli.convert_currency", return_value=90.0)
    @patch("builtins.print")
    def test_fixed_mode_conversion(self, mock_print, mock_convert, mock_input):
        app_cli.fixed_mode()
        mock_convert.assert_called_with(100.0, "USD", "EUR")
        mock_print.assert_any_call("100.0 USD = 90.00 EUR")

    @patch("builtins.input", side_effect=["6", "50", "0"])
    @patch("app_cli.get_all_conversions", return_value={"USD": 0.0032, "EUR": 0.0028, "JPY": 4.6})
    @patch("builtins.print")
    def test_fixed_mode_all_from_idr(self, mock_print, mock_get_all, mock_input):
        app_cli.fixed_mode()
        mock_get_all.assert_called_with(50.0, "IDR")
        mock_print.assert_any_call("50.0 IDR = 0.0032 USD")

if __name__ == "__main__":
    unittest.main(verbosity=2)