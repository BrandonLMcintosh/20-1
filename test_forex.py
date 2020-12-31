import time
from decimal import Decimal
from logging import error
from types import ClassMethodDescriptorType
from forex import Forex
from unittest import TestCase

class TestHelpers():
    @staticmethod
    def search_list(list, query):
        if any(query in item for item in list):
            return True
        return False

class CheckValuesCase(TestCase):
    def setUp(self):
        time.sleep(.5)
        pass

    def test_bad_code_in_check(self):
        errors, unused = Forex.check_values("USD", "ZZZ", "14")
        self.assertIs(TestHelpers.search_list(errors, "Invalid currency code"), True)

    def test_bad_amount_in_check(self):
        errors, unused = Forex.check_values("USD", "USD", "$$$")
        self.assertIs(TestHelpers.search_list(errors, "Invalid amount"), True)

    def test_good_values_in_check(self):
        errors, unused = Forex.check_values("USD", "USD", "14")
        self.assertIs(TestHelpers.search_list(errors, "Invalid currency code"), False)
        self.assertIs(TestHelpers.search_list(errors, "Invalid amount"), False)

class CheckInstanceCreation(TestCase):
    def test_bad_code_in_instance(self):
        currencies = Forex("USD", "ZZZ", "14")
        self.assertEqual(currencies.from_currency["amount"], 14.0)
        self.assertEqual(currencies.from_currency["symbol"], "US$")
        self.assertEqual(currencies.from_currency["name"], "United States dollar")
        self.assertEqual(currencies.from_currency["code"], "USD")
        
        self.assertEqual(currencies.to_currency["amount"], "ERROR: ONE OR MORE BAD CODES")
        self.assertEqual(currencies.to_currency["symbol"], "BAD CODE")
        self.assertEqual(currencies.to_currency["name"], "BAD CODE")
        self.assertEqual(currencies.to_currency["code"], "ZZZ")
    def test_bad_amount_in_instance(self):
        currencies = Forex("USD", "USD", "$$$$")
        self.assertEqual(currencies.from_currency["amount"], 1.0)
        self.assertEqual(currencies.from_currency["symbol"], "US$")
        self.assertEqual(currencies.from_currency["name"], "United States dollar")
        self.assertEqual(currencies.from_currency["code"], "USD")
        
        self.assertEqual(currencies.to_currency["amount"], 1.0)
        self.assertEqual(currencies.to_currency["symbol"], "US$")
        self.assertEqual(currencies.to_currency["name"], "United States dollar")
        self.assertEqual(currencies.to_currency["code"], "USD")

    def test_good_values_in_instance(self):
        currencies = Forex("USD", "USD", "14")
        self.assertEqual(currencies.from_currency["amount"], 14.0)
        self.assertEqual(currencies.from_currency["symbol"], "US$")
        self.assertEqual(currencies.from_currency["name"], "United States dollar")
        self.assertEqual(currencies.from_currency["code"], "USD")
        
        self.assertEqual(currencies.to_currency["amount"], 14.0)
        self.assertEqual(currencies.to_currency["symbol"], "US$")
        self.assertEqual(currencies.to_currency["name"], "United States dollar")
        self.assertEqual(currencies.to_currency["code"], "USD")


