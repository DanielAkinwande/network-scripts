from flask import Flask, jsonify
from health_checker import run_checks

app = Flask(__name__)

@app.route("/status")
def status():
    data = run_checks()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)