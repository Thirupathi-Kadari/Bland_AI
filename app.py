# Install the Flask library
# pip install flask

from flask import Flask, request, jsonify
import json
import os

# Initialize Flask application
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Endpoint to handle incoming webhook requests from the Bland API.
    
    The webhook expects JSON data, which is printed and saved to a file for storage.
    
    Returns:
        JSON response indicating success.
    """
    data = request.json
    print("Webhook received data:", data)
    
    # Append the received data to the 'conversations.json' file
    # In a production environment, consider using a database for better scalability and performance.
    with open('conversations.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
    
    return jsonify({"status": "success"}), 200

@app.route('/conversations', methods=['GET'])
def get_conversations():
    """
    Endpoint to retrieve stored conversations.
    
    Reads data from the 'conversations.json' file and returns it as a JSON array.
    If the file does not exist, returns an error message.
    
    Returns:
        JSON array of stored conversations or an error message if no conversations are found.
    """
    if os.path.exists('conversations.json'):
        with open('conversations.json', 'r') as f:
            conversations = f.readlines()
        
        # Convert each line in the file from JSON string to Python dictionary
        conversations = [json.loads(conv) for conv in conversations]
        return jsonify(conversations), 200
    else:
        return jsonify({"error": "No conversations found"}), 404

if __name__ == '__main__':
    # Run the Flask application on port 5000 with debugging enabled
    app.run(port=5000, debug=True)