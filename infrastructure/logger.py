import json
from datetime import datetime

def log_event(event_type, data):
    timestamp = datetime.now().isoformat()
    entry = {
        "timestamp": timestamp,
        "event": event_type,
        "data": data
    }
    with open("robot_log.txt", "a") as f:
        f.write(json.dumps(entry) + "\n")
