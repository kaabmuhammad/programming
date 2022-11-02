from flask import Flask, render_template, request, url_for, flash, redirect, json
from roman_numeral_converter import *


app: Flask = Flask(__name__)


cal = []


@app.route("/")
def index():
    return render_template("index.html", message=cal)


@app.route("/home/", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        num = int(request.form["number"])

        cal.insert(0, to_roman_numeral(num))
        string = request.form["roman"]

        cal.insert(1, to_arabic_number(string))

        return redirect(url_for("index"))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=2000)
