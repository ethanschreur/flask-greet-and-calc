# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/<operation>')
def calc_func(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    operations_dict = {'add': add(a, b), 'sub': sub(a,b), 'mult': mult(a,b), 'div': div(a,b)}
    return str(operations_dict.get(operation, None))
