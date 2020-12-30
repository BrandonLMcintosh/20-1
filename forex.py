from forex_python.converter import CurrencyCodes, CurrencyRates
class Forex:
    
    def __init__(self, to_code, from_code, amount):
        self.from_code = from_code
        self.to_code = to_code
        self.amount = float(amount)
        self.from_currency = self.currency(self.from_code, self.amount)
        self.to_currency = self.currency(self.to_code, CurrencyRates().convert(self.from_code, self.to_code, self.amount))

    def currency(self, code, amount):
        this_currency = {}
        this_currency["symbol"] = CurrencyCodes().get_symbol(code) 
        this_currency["name"] = CurrencyCodes().get_currency_name(code)
        this_currency["amount"] = amount
        this_currency["code"] = code
        return this_currency

    @classmethod
    def check_values(cls, amount, from_code, to_code):
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
        except ValueError:
            return f"Invalid amount '{amount}'. Please use a whole number or decimal greater than 0"

    @staticmethod
    def check_code(code):
        if CurrencyCodes().get_symbol(code) is not None:
            pass
        else:
            return f"Invalid currency code '{code}'. Please verify currency code and try again"
            