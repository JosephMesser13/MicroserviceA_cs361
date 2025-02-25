# test_client.py
import requests
import datetime

BASE_URL = "http://128.193.36.2:8080"

def test_create_event():
    payload = {
        "event_name": "Debut Stream",
        "vtuber_name": "Kekoa VTuber",
        "start_time": (datetime.datetime.now() + datetime.timedelta(minutes=45)).isoformat()
    }
    response = requests.post(f"{BASE_URL}/events", json=payload)
    print("Create Event Response:", response.json())

def test_list_events():
    response = requests.get(f"{BASE_URL}/events")
    print("List Events Response:", response.json())

def test_get_notifications():
    response = requests.get(f"{BASE_URL}/notifications")
    print("Notifications Response:", response.json())

if __name__ == '__main__':
    print("Running Tests...")
    test_create_event()
    test_list_events()
    test_get_notifications()
