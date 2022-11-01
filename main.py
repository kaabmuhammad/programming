from flask import Flask, render_template, request, url_for, flash, redirect, json
from roman_numeral_converter import *

app: Flask = Flask(__name__)


values = [{}]


@app.route("/")
def index():
    return render_template("index.html", message=values)


@app.route("/home/", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        num = int(request.form["title"])
        cal = []

        cal.append({num: to_roman_numeral(num)})
        string = request.form["content"]

        cal.append({string: to_arabic_number(string)})
        values.append(cal)
        return redirect(url_for("index"))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=2000)
