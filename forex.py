from forex_python.converter import CurrencyCodes, CurrencyRates

class Forex:
    def __init__(self, to_code, from_code, amount):
        self.from_code = from_code
        self.to_code = to_code
        self.amount = amount
        self.to_currency = self.currency(self.to_code, self.amount)
        self.from_currency = self.currency(self.from_code, self.convert_currency(self.to_code, self.from_code, self.amount))
        self.r = CurrencyRates()
        self.c = CurrencyCodes()

    def currency(self, code, amount):
        this_currency = {}
        this_currency["symbol"] = self.c.get_symbol(code)
        this_currency["name"] = self.c.get_currency_name(code)
        this_currency["amount"] = amount
        this_currency["code"] = code
        return this_currency
    
    def convert_currency(self, from_code, to_code, amount):
        new_amount = self.r.convert(from_code, to_code, amount)
        return new_amount

    def check_values():
        return
        # Need to check for: 
        #     valid codes
        #     valid amounts