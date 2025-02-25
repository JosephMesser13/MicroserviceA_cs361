# microservice.py
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory storage for events
events = []

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event_name = data.get('event_name')
    vtuber_name = data.get('vtuber_name')
    start_time = data.get('start_time')

    try:
        parsed_time = datetime.fromisoformat(start_time)
    except ValueError:
        return jsonify({"error": "Invalid time format. Use ISO 8601."}), 400

    event = {
        'id': len(events) + 1,
        'event_name': event_name,
        'vtuber_name': vtuber_name,
        'start_time': parsed_time.isoformat()
    }
    events.append(event)
    return jsonify(event), 201

@app.route('/events', methods=['GET'])
def list_events():
    return jsonify(events), 200

@app.route('/notifications', methods=['GET'])
def get_notifications():
    now = datetime.now()
    soon_events = [
        event for event in events
        if datetime.fromisoformat(event['start_time']) - now <= timedelta(minutes=30)
    ]
    return jsonify(soon_events), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
