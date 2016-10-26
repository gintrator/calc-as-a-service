from flask import Flask
from flask import request
import json
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)


def calculate(x, y, op):
    if op == 'add':
        return x + y
    elif op == 'subtract':
        return x - y
    elif op == 'multiply':
        return x * y
    elif op == 'divide':
        return x / y
    else:
        return None

@app.route('/caas', methods=['POST'])
def calc_endpoint():
    x = request.args.get('x')
    y = request.args.get('y')
    op = request.args.get('op')
    if not (x and y and op):
        return json.dumps({'error': 'Missing an operand or operator.'}), 500
    try:
        result = calculate(float(x), float(y), op)
    except ValueError as e:
        return json.dumps({'error': 'Operand must be a number.'}), 500
    if result is None:
        return json.dumps({'error': 'Invalid operator.'}), 500
    return json.dumps({'result': result})


def main():
    handler = RotatingFileHandler('logs/caas.log', maxBytes=1024*10, backupCount=10)
    handler.setLevel(logging.INFO)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    log.addHandler(handler)
    app.run(host='0.0.0.0', debug=False)

if __name__ == '__main__':
    main()
