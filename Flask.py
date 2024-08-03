from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook received data:", data)
    
    # Save the data to a JSON file
    with open('call_data.json', 'w') as f:
        json.dump(data, f)
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5000)