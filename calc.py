import json
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import request
from operator import add, sub, mul, div

app = Flask(__name__)

OPS = {'add': add, 'subtract': sub, 'multiply': mul, 'divide': div}
ERROR = 'error'
RESULT = 'result'

@app.route('/equals', methods=['POST'])
def calc_endpoint():
    x = request.args.get('x')
    y = request.args.get('y')
    op = request.args.get('op')
    if not (x and y and op):
        return json.dumps({ERROR: 'Missing an operand or operator.'}), 500
    if op not in OPS:
        return json.dumps({ERROR: 'Invalid operator.'}), 500
    try:
        result = OPS[op](float(x), float(y))
    except ValueError as e:
        return json.dumps({ERROR: 'Operands must be numbers.'}), 500
    return json.dumps({RESULT: result})


def main():
    handler = RotatingFileHandler('logs/caas.log', maxBytes=1024*10, backupCount=10)
    handler.setLevel(logging.INFO)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    log.addHandler(handler)
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    main()

