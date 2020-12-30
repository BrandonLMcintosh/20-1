from flask import Flask, render_template, request, flash, redirect
from forex import Forex


app = Flask(__name__)
app.config["SECRET_KEY"] = "SuperSecret"

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/", methods=["POST"])
def return_amount():
    from_code = request.form["from"]
    to_code = request.form["to"]
    amount = request.form["amount"]
    errors, needs_redirect = Forex.check_values(amount, from_code, to_code)
    if needs_redirect:
        for error in errors:
            if error is not None:
                flash(error)
        return redirect("/")
    currencies = Forex(to_code, from_code, amount)
    return render_template("returnAmount.html", currencies = currencies)



