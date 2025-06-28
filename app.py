from flask import Flask, request, jsonify
from event_manager import *

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Event Scheduler API is running!", 200

@app.route("/events", methods=["POST"])
def create_event():
    data = request.json
    event = add_event(data)
    return jsonify(event), 201

@app.route("/events", methods=["GET"])
def list_events():
    return jsonify(get_all_events()), 200

@app.route("/events/<event_id>", methods=["PUT"])
def update(event_id):
    updated = update_event(event_id, request.json)
    if updated:
        return jsonify(updated), 200
    return jsonify({"error": "Event not found"}), 404

@app.route("/events/<event_id>", methods=["DELETE"])
def delete(event_id):
    if delete_event(event_id):
        return jsonify({"message": "Deleted successfully"}), 200
    return jsonify({"error": "Event not found"}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)