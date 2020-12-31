from app import app
from unittest import TestCase
import html

def response_to_string(response):
    """
    Converts response to readable text for easier testing of HTML
    """
    html_string = response.get_data(as_text=True)
    html_string = html.unescape(html_string)
    html_string = html_string.replace("\n", "")
    return html_string

class AppTestGetRequestCase(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        html_response = response_to_string(response)
        self.assertIn('<input type="text" class="form-control" name="amount" id="amount" />', html_response)

class AppTestPostRequestCase(TestCase):

    def setUp(self):
        self.client = app.test_client()
    def test_bad_codes(self):
        bad_to = "ZZZ"
        bad_from = "YYY"
        good_amount = "13"
        params = {"amount": good_amount, "to": bad_to, "from": bad_from}
        response = self.client.post("/", data=params, follow_redirects=True)
        html_response = response_to_string(response)
        self.assertIn(f"Invalid currency code '{bad_to}'", html_response)
        self.assertIn(f"Invalid currency code '{bad_from}'", html_response)
        self.assertNotIn("Invalid amount", html_response)
        
    def test_bad_amount(self):
        good_to = "USD"
        good_from = "AUD"
        bad_amount = "MONEY"
        params = {"amount": bad_amount, "to": good_to, "from": good_from}
        response = self.client.post("/", data=params, follow_redirects=True)
        html_response = response_to_string(response)
        self.assertNotIn(f"Invalid currency code '{good_to}'", html_response)
        self.assertNotIn(f"Invalid currency code '{good_from}'", html_response)
        self.assertIn(f"Invalid amount '{bad_amount}'", html_response)

    def test_good_values(self):
        good_to = "USD"
        good_from = "USD"
        good_amount = "14"
        params = {"amount": good_amount, "to": good_to, "from": good_from}
        response = self.client.post("/", data=params)
        html_response = response_to_string(response)
        self.assertNotIn("Invalid", html_response)
        self.assertIn("US$14.0  United States dollar to United States dollar is  US$14.0", html_response)
    
