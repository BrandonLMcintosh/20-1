from logging import error
from forex_python.converter import CurrencyCodes, CurrencyRates
class Forex:
    
    def __init__(self, from_code, to_code, amount):
        self.from_code = from_code
        self.to_code = to_code
        self.amount = self.try_float(amount)
        self.to_amount = self.try_convert(self.from_code, self.to_code, self.amount)
        self.from_currency = self.currency(self.from_code, self.amount)
        self.to_currency = self.currency(self.to_code, self.to_amount)

    def currency(self, code, amount):
        this_currency = {}
        currency_symbol = CurrencyCodes().get_symbol(code)
        currency_name = CurrencyCodes().get_currency_name(code)
        if currency_symbol:
            this_currency["symbol"] = currency_symbol
        else:
            this_currency["symbol"] = "BAD CODE"
        
        if currency_name:
            this_currency["name"] = currency_name
        else:
            this_currency["name"] = "BAD CODE"

        this_currency["amount"] = amount
        this_currency["code"] = code
        return this_currency

    @classmethod
    def check_values(cls, from_code, to_code, amount):
        alerts = []
        bad_amount = cls.check_amount(amount)
        bad_from_code = cls.check_code(from_code)
        bad_to_code = cls.check_code(to_code)
        needs_redirect = False
        if bad_amount:
            alerts.append(bad_amount)
            needs_redirect = True
        if bad_from_code:
            alerts.append(bad_from_code)
            needs_redirect = True
        if bad_to_code:
            alerts.append(bad_to_code)
            needs_redirect = True
        return alerts, needs_redirect

    @staticmethod
    def check_amount(amount):
        try: 
            float(amount)
            pass
        except:
            return f"Invalid amount '{amount}'. Please use a whole number or decimal greater than 0"

    @staticmethod
    def check_code(code):
        if CurrencyCodes().get_symbol(code) is not None:
            pass
        else:
            return f"Invalid currency code '{code}'. Please verify currency code and try again"
    
    def try_float(self, amount):
        if self.check_amount(amount):
            amount = 1.0
        else:
            amount = float(amount)
        return amount
    
    def try_convert(self, from_code, to_code, amount):
        try:
            new_amount = CurrencyRates().convert(from_code, to_code, amount)
            return new_amount
        except:
            return "ERROR: ONE OR MORE BAD CODES"