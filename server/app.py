#!/usr/bin/env python3

from flask import Flask, request, session, jsonify, make_response

# Initialize Flask app
app = Flask(__name__)
app.json.compact = False  # Makes JSON responses pretty-printed

# Secret key is required for sessions to work
app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    """
    Display a session value and cookies for the given key.
    Sets default session values if they do not exist.
    Sets a cookie named 'mouse'.
    """
    # Initialize session values only if they don't exist
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Build response JSON containing session info and current cookies
    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]} for cookie in request.cookies],
    }), 200)

    # Set a cookie called 'mouse' with value 'Cookie'
    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    # Run the Flask server on port 5555
    app.run(port=5555)
