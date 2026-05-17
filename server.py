# Import utilities and helper files
from flask import Flask, jsonify, request, make_response, send_from_directory
from flask_cors import CORS
from data import get_sample_data

app = Flask(__name__, static_folder="../client", static_url_path='')
CORS(app)

# Get the data from data.py for in memory list new posts are appeneded here
events = get_sample_data()

"""
Create a route for "/" it serves the index.html files from the client folder. This route should return a JSON welcome message. Make sure to use decorator and create a proper function.
"""
@app.route("/", methods=["GET"])
def welcome():
    return send_from_directory(app.static_folder, "index.html")

"""
Create a GET route for "/events". This route should return the full list of events as JSON. The front end will fetch on page load to display the events list. Respond with 200 - ok.
"""
@app.route("/events/data", methods=["GET"])
def display_events():
    return make_response(jsonify(events), 200)

"""
Create a POST route for "/events": This route should:
    1. Get the JSON data from the request
    2. Validate that "title" is provided
    3. Create a new event with a unique ID and the provided title
    4. Add the new event to the events list
    5. Return the new event with status code 201
"""
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # Error handling and control flow to see if the data or event exists in the request
    if not data or "title" not in data:
        return make_response(jsonify({"error": "Title is required"}), 400)
    
    # Create unique ID 
    new_id = max(e["id"] for e in events) + 1 if events else 1

    # Create new event object
    new_event = {
        "id": new_id,
        "title": data["title"]
    }

    # append it to out events object in already in memory
    events.append(new_event)

    # Return the new event with 201
    return make_response(jsonify(new_event), 201)
    

if __name__ == "__main__":
    app.run(port=5555, debug=True)
