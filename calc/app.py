from flask import Flask, request 
import operations

app = Flask(__name__)


@app.route("/add")
def add():
    a = request.args["a"]
    b = request.args["b"]
    total = operations.add(int(a), int(b))
    return f"""<p>{total}</p>"""


@app.route("/sub")
def sub():
    a = request.args["a"]
    b = request.args["b"]
    total = operations.sub(int(a), int(b))
    return f"""<p>{total}</p>"""


@app.route("/mult")
def mult():
    a = request.args["a"]
    b = request.args["b"]
    total = operations.mult(int(a), int(b))
    return f"""<p>{total}</p>"""


@app.route("/div")
def div():
    a = request.args["a"]
    b = request.args["b"]
    total = operations.div(int(a), int(b))
    return f"""<p>{total}</p>"""