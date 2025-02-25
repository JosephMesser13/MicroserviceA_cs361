# CS361 Microservice A: VTuber Event Notification Microservice

This microservice provides notifications for VTuber events occurring soon. It is part of a larger application designed to keep users informed about scheduled events.

## Author: Kekoa Young
## Designed for: Joseph

## Features
- Retrieve a list of VTuber events happening within the next 30 minutes.
- Simple REST API interface.

## Technologies Used
- Python
- Flask

---

## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd vtuber-notification-microservice
    ```

2. **Install Dependencies**:
    Make sure you have Python 3.8 or later installed.
    ```bash
    pip install flask
    ```

3. **Run the Microservice**:
    ```bash
    python vtuber_notification.py
    ```

The microservice will run locally on `http://127.0.0.1:5002`.

---

## API Usage

### Endpoint
**GET /notify**

#### Description:
Returns a list of VTuber events scheduled to occur within the next 30 minutes.

#### Example Request:
```bash
curl http://127.0.0.1:5000/notify
```

#### Example Response:
- If there are upcoming events:
```json
{
  "status": "success",
  "upcoming_events": [
    {
      "id": 1,
      "name": "VTuber Concert",
      "time": "2025-02-26T18:00:00",
      "description": "Live performance by VTuber XYZ."
    }
  ]
}
```

- If no events are occurring soon:
```json
{
  "status": "success",
  "message": "No events occurring soon."
}
```

---

## Mitigation Plan for Integration

1. **Potential Challenges**:
    - **Network Issues**: Ensure the main program retries failed requests up to three times with exponential backoff.
    - **Event Format Mismatch**: Validate response data structure using schema libraries like `pydantic` or `jsonschema` in the main program.

2. **Testing the Integration**:
    - Simulate various scenarios (upcoming events, no events, invalid responses) with automated test cases.

3. **Fallback Plan**:
    - If the microservice is unavailable, display a cached list of events or a friendly error message to users.

---

## Future Enhancements
- Extend functionality to support event filtering (e.g., by VTuber name).
- Implement push notifications for real-time updates.
- Add persistent data storage (e.g., SQLite or MongoDB) for event information.

---

For questions contact me at youngkek@oregonstate.edu.

