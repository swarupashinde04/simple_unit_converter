from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        value = float(request.form["value"])
        conversion = request.form["conversion"]

        if conversion == "km_to_m":
            result = value * 1000

        elif conversion == "kg_to_g":
            result = value * 1000

        elif conversion == "c_to_f":
            result = (value * 9/5) + 32

    return render_template("index.html", result=result)

app.run(debug=True)