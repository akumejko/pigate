import signal
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

# Define a list of authorized API keys
authorized_keys = {
    "your_api_key": "your_username",
    # Add more keys as needed
}

def authenticate_api_key():
    api_key = request.headers.get('X-API-Key')
    if api_key in authorized_keys:
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/openGate', methods=['POST'])
def open_gate():
    # Check for API key authentication
    if not authenticate_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    # Your logic for opening the gate goes here
    # For now, let's just print a message
    print("Gate opened!")

    return jsonify({"status": "Gate opened!"})

def handle_exit(signum, frame):
    print(f"Received signal {signum}. Exiting gracefully.")
    # Perform cleanup actions if needed
    # ...

    # Exit the application
    exit(0)

if __name__ == '__main__':
    # Register the signal handler
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    # Start the Flask application
    app.run(host='0.0.0.0', port=5001, debug=True)
