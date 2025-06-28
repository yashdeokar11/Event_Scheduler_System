from event_manager import add_event, get_all_events

def test_add_event():
    data = {
        "title": "Test Event",
        "description": "Test Desc",
        "start_time": "2025-06-28 10:00",
        "end_time": "2025-06-28 11:00"
    }
    event = add_event(data)
    assert event["title"] == "Test Event"
    assert len(get_all_events()) >= 1