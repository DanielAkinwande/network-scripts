from flask import Flask, request, jsonify
import requests
import time
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Health checker is running!"

@app.route("/check")
def check():
    url = request.args.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        latency = round((time.time() - start) * 1000, 2)

        return jsonify({
            "url": url,
            "status_code": response.status_code,
            "latency_ms": latency
        })

    except Exception as e:
        return jsonify({
            "url": url,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)