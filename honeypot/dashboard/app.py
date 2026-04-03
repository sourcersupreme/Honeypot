from flask import Flask, render_template
import json

app = Flask(__name__)

LOG_FILE = "../logs/attacks.json"

@app.route("/")
def index():
    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    total = len(data)
    unique_ips = len(set([entry["ip"] for entry in data]))

    return render_template("index.html", data=data, total=total, unique_ips=unique_ips)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
