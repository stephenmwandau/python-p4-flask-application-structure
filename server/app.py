#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(f"{parameter}")
    return f"{parameter}"

@app.route("/count/<int:parameter>")
def count(parameter):
    result = ""
    for number in range(parameter):
        result += f"{number}\n"
    return result

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            return f"Error: Division by zero is not allowed."
        else:
            result = num1 / num2
    elif operation == "mod":
        result = num1 % num2
    else:
        return f"0"
    
    return f"{result}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)