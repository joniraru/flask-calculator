from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

@app.route('/')
def index():
    return "Калькулятор работает! Используйте /calculate для вычислений."

@app.route('/calculate', methods=['GET'])
def calculate():
    operation = request.args.get('operation')
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        return jsonify({"error": "Invalid operation"}), 400

    log_operation(operation, num1, num2, result)
    return jsonify({"result": result})

def log_operation(operation, num1, num2, result):
    LOG_FILE = '/app/data/logs.txt'
    with open(LOG_FILE, 'a') as f:
        f.write(f"{operation} {num1} {num2} = {result}\n")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

