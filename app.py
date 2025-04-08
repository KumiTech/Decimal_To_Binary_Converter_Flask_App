#Imports
from flask import Flask
from flask import render_template
from flask import url_for 
from flask import request


#My App
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    binary_output = None
    decimal_input = None
    if request.method == 'POST':
        decimal_input = request.form['decimal_number']
        binary_output = decimal_to_binary(decimal_input)
    return render_template('index.html', binary_output=binary_output, decimal_input=decimal_input)



def decimal_to_binary(decimal_num):
    """Converts a decimal integer to its binary representation."""
    try:
        num = int(decimal_num)
        if num < 0:
            return "Binary representation of negative numbers is not supported in this simple example."
        elif num == 0:
            return "0"
        else:
            binary = ""
            while num > 0:
                remainder = num % 2
                binary = str(remainder) + binary
                num //= 2
            return binary
    except ValueError:
        return "Invalid input. Please enter a valid integer."


if __name__ in "__main__":
    app.run(debug=True)