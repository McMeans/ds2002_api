from flask import Flask, jsonify, request
import pytz
from datetime import datetime

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

CAPITAL_TIMEZONES = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Moscow": "Europe/Moscow",
    "Beijing": "Asia/Shanghai",
    "Berlin": "Europe/Berlin",
    "Rome": "Europe/Rome",
    "Madrid": "Europe/Madrid"
}

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/api/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({"secret": "This is protected info!"})

@app.route('/api/capital-time/<city>', methods=['GET'])
@token_required
def get_capital_time(city):
    if city not in CAPITAL_TIMEZONES:
        return jsonify({
            "error": "City not found",
            "message": f"Sorry, {city} is not in our database. Available cities are: {', '.join(CAPITAL_TIMEZONES.keys())}"
        }), 404
    
    timezone = pytz.timezone(CAPITAL_TIMEZONES[city])
    current_time = datetime.now(timezone)
    utc_offset = current_time.strftime('%z')
    
    return jsonify({
        "city": city,
        "local_time": current_time.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": utc_offset,
        "timezone": CAPITAL_TIMEZONES[city]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)