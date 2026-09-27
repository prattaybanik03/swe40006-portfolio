import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return (
        "<h1>SWE40006 — Task 4.2</h1>"
        f"<p>Served by container <code>{socket.gethostname()}</code></p>"
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))