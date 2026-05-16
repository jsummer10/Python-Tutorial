""" An introduction to python web applications with Flask """

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/greet/<name>")
def greet(name):
    return jsonify({
        "message": f"Hello, {name}!"
    })


@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()

    a = data.get("a", 0)
    b = data.get("b", 0)

    return jsonify({
        "a": a,
        "b": b,
        "sum": a + b
    })


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=10001, debug=True)