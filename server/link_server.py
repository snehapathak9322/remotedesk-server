from flask import Flask, redirect

app = Flask(__name__)

@app.route("/connect/<device_id>")
def connect(device_id):
    return f"Connecting to device {device_id}"

app.run(host="0.0.0.0", port=5000)