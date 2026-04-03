import json
from datetime import datetime

LOG_FILE = "logs/attacks.json"

def log_attack(ip, username, password):
    log_entry = {
        "ip": ip,
        "username": username,
        "password": password,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[LOGGED] {ip} -> {username}:{password}")
