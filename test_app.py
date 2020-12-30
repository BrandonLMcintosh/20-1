from werkzeug import datastructures
from app import app
from unittest import TestCase



class AppTestGetRequestCase(TestCase):

    def test_home(self):
        response = self.client.get("/")
        html = response.get_data(as_text = True)
        self.assertIn('<input type="text" class="form-control" name="amount" id="amount" />', html)

class AppTestPostRequestCase(TestCase):
    def test_bad_codes(self):
        bad_to = "ZZZ"
        bad_from = "YYY"
        good_amount = "13"
        params = {"amount": good_amount, "to": bad_to, "from": bad_from}
        response = self.client.post("/", data=params, follow_redirects=True)
        html = response.get_data(as_text=True)
        self.assertIn(f"Invalid currency code '{bad_to}'", html)
        self.assertIn(f"Invalid currency code '{bad_from}'", html)
        self.assertNotIn("Invalid amount", html)
        
    def test_bad_amount(self):
        good_to = "USD"
        good_from = "AUD"
        bad_amount = "MONEY"
        params = {"amount": bad_amount, "to": good_to, "from": good_from}
        response = self.client.post("/", data=params, follow_redirects=True)
        html = response.get_data(as_text=True)
        self.assertNotIn(f"Invalid currency code '{good_to}'", html)
        self.assertNotIn(f"Invalid currency code '{good_from}'", html)
        self.assertIn(f"Invalid amount '{bad_amount}'", html)

    def test_good_values(self):
        good_to = "USD"
        good_from = "USD"
        good_amount = "14"
        params = {"amount": good_amount, "to": good_to, "from": good_from}
        response = self.client.post("/", data=params)
        html = response.get_data(as_text=True)
        self.assertNotIn("Invalid", html)
        self.assertIn("US$14 United States Dollar to ", html)