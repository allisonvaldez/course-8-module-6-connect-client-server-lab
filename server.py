# Import utilities and helper files
from flask import Flask, jsonify, request
from flask_cors import CORS
from data import get_sample_data

app = Flask(__name__, static_folder='../client', static_url_path='')
CORS(app)

"""
Create a route for "/". This route should return a JSON welcome message. Make sure to use decorator and create a proper function.
"""
@app.route("/", methods=["GET"])
def welcome():
    return send_from_directory(app.static_folder, "index.html")

"""
Create a GET route for "/events". This route should return the full list of events as JSON.
"""

"""
Create a POST route for "/events": This route should:
    1. Get the JSON data from the request
    2. Validate that "title" is provided
    3. Create a new event with a unique ID and the provided title
    4. Add the new event to the events list
    5. Return the new event with status code 201
"""

if __name__ == "__main__":
    app.run(port=5555, debug=True)
