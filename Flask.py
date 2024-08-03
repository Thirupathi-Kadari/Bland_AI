pip install flask

from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook received data:", data)
    
    # Save the data to a JSON file (or use a database for scalability)
    with open('conversations.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
    
    return jsonify({"status": "success"}), 200

@app.route('/conversations', methods=['GET'])
def get_conversations():
    # Read the conversations from the JSON file
    if os.path.exists('conversations.json'):
        with open('conversations.json', 'r') as f:
            conversations = f.readlines()
        
        # Parse each line as a JSON object
        conversations = [json.loads(conv) for conv in conversations]
        return jsonify(conversations), 200
    else:
        return jsonify({"error": "No conversations found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
