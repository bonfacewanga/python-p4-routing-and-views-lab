#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

from flask import Flask

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route for printing a string
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  
    # Print the text to the console
    # Return the text to be displayed in the browser
    return text

# Route for counting up to a number
@app.route('/count/<int:number>')
def count(number):
    # Generate a range of numbers and join them with newline characters
    # Ensure a newline character at the end
    return '\n'.join(str(i) for i in range(number)) + '\n'

# Route for performing mathematical operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        # Return 400 Bad Request for invalid operation
        return "Invalid operation", 400  

    return str(result)

if __name__ == '__main__':
    # Now run the Flask app on port 5555
    app.run(port=5555)  
