from flask import Flask, render_template, request
from vm import VendingMachine
app = Flask(__name__)

vm = None
@app.route("/")
def init():
    vm = VendingMachine([])
    html = render_template('index.html')
    return html

@app.route("/get_items", methods=["POST"])
def get_items():
    return vm.get_items()

# @app.route("", methods=["POST"])
