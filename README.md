# Event Scheduler System

This is a simple Flask-based backend application to manage events (create, view, update, delete).

## 🏁 How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Start the server:
```
python app.py
```

3. Use Postman to test these APIs:
- `POST /events` - create an event
- `GET /events` - list all events
- `PUT /events/<id>` - update event by ID
- `DELETE /events/<id>` - delete event by ID

### Sample POST body:
```json
{
  "title": "Meeting with client",
  "description": "Quarterly review at 4 PM",
  "start_time": "2025-06-28 16:00",
  "end_time": "2025-06-28 17:00"
}
```
