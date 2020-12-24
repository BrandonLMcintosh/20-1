from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex import Forex
from decimal import Decimal
c = CurrencyRates(force_decimal=True)
s = CurrencyCodes()
app = Flask(__name__)
app.config["SECRET_KEY"] = "SuperSecret"

@app.route("/")
def form():
    return render_template("form.html")
@app.route("/", methods=["POST"])
def return_amount():
    from_code = request.form["from"]
    to_code = request.form["to"]
    amount = float(request.form["amount"])
    currencies = Forex(to_code, from_code, amount)
    return render_template("returnAmount.html", currencies = currencies)



