import json
import os
import uuid
from datetime import datetime


EVENT_FILE = 'event_scheduler/storage.json'

def load_events():
    try:
        with open(EVENT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_events(events):
    os.makedirs(os.path.dirname(EVENT_FILE), exist_ok=True)
    with open(EVENT_FILE, "w") as f:
        json.dump(events, f, indent=4)

def add_event(data):
    required_fields = ["title", "description", "start_time", "end_time"]
    for field in required_fields:
        if field not in data or not data[field]:
            raise ValueError(f"Missing or empty field: {field}")

    try:
        datetime.strptime(data["start_time"], "%Y-%m-%d %H:%M")
        datetime.strptime(data["end_time"], "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD HH:MM'.")

    events = load_events()

    new_event = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "description": data["description"],
        "start_time": data["start_time"],
        "end_time": data["end_time"]
    }

    events.append(new_event)
    save_events(events)
    return new_event


def get_all_events():
    return sorted(load_events(), key=lambda e: e["start_time"])

def update_event(event_id, data):
    events = load_events()
    for event in events:
        if event["id"] == event_id:
            event.update(data)
            save_events(events)
            return event
    return None

def delete_event(event_id):
    events = load_events()
    updated_events = [e for e in events if e["id"] != event_id]
    if len(updated_events) != len(events):
        save_events(updated_events)
        return True
    return False