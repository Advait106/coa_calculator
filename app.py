from flask import Flask, render_template, request
from coa_project import add_strings, subtract_strings, multiply_strings, divide_strings, compare
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        num1 = request.form["num1"].strip()
        num2 = request.form["num2"].strip()
        op = request.form["operation"]

        if op == "+":
            result = add_strings(num1, num2)
        elif op == "-":
            if compare(num1, num2) >= 0:
                result = subtract_strings(num1, num2)
            else:
                result = "-" + subtract_strings(num2, num1)
        elif op == "*":
            result = multiply_strings(num1, num2)
        elif op == "/":
            result = divide_strings(num1, num2)
        else:
            result = "Invalid operation"
    return render_template("index.html", result=result)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

