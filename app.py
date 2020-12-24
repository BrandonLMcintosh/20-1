from flask import Flask
from flask import render_template, request, redirect
from forex_python.converter import CurrencyRates

app = Flask(__name__)
app.config["SECRET_KEY"] = "SuperSecret"

@app.route("/")
def form():
    return render_template("form.html")
@app.route("/", methods=["POST"])
def returnConvert():
    from_currency = request.form["from"]
    to_currency = request.form["to"]
    amount = request.form["amount"]
    newAmount = CurrencyRates.convert(from_currency, to_currency, amount)
    return redirect("return.html")

