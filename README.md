# Bland_AI
# Reminder Call Project

This project uses the Bland API to make reminder calls and sets up a Flask server to handle webhooks and store conversations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.6+
- `requests` library
- `flask` library
- `ngrok` (for HTTPS tunneling)

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/reminder-call-project.git
    cd reminder-call-project
    ```

2. Install the dependencies:
    ```sh
    pip install requests
    pip install flask
    ```

## Usage

### Making a Reminder Call

To make a reminder call using the Bland API, refer to the [Bland_Ai_Integ.ipynb](https://github.com/Thirupathi-Kadari/Bland_AI/blob/main/Bland_Ai_Integ.ipynb) file in the repository.

### Setting Up the Flask Server

To set up the Flask server to handle webhooks and store conversations, refer to the [Flask.py](path/to/your/flask_server.py) file in the repository.

### Using ngrok for HTTPS

Since the `remainder_call.py` file requires an HTTPS URL but the Flask server provides only HTTP, you can use ngrok to create an HTTPS tunnel. Follow these steps:

1. Install ngrok:
    ```sh
    # On macOS
    brew install ngrok/ngrok/ngrok

    # On Windows
    choco install ngrok

    # On Linux
    snap install ngrok
    ```

2. Start the Flask server:
    ```sh
    python flask_server.py
    ```

3. In a new terminal, start ngrok to tunnel your Flask server:
    ```sh
    ngrok http 5000
    ```

4. Copy the HTTPS URL provided by ngrok (e.g., `https://<your-subdomain>.ngrok.io`) and use it as the webhook URL in your `reminder_call.py` file.

## API Documentation

### POST /webhook

- **Description**: Handles incoming webhook data.
- **Method**: POST
- **Request Body**: JSON object with the data sent by the Bland API.
- **Response**: 
    - Success: `{"status": "success"}`
    - Failure: `{"status": "failure"}`

### GET /conversations

- **Description**: Retrieves stored conversations.
- **Method**: GET
- **Response**: 
    - Success: JSON array of conversations
    - Failure: `{"error": "No conversations found"}`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
