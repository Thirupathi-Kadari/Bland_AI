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

To make a reminder call using the Bland API, refer to the [reminder_call.py](path/to/your/reminder_call.py) file in the repository.

### Setting Up the Flask Server

To set up the Flask server to handle webhooks and store conversations, refer to the [flask_server.py](path/to/your/flask_server.py) file in the repository.

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


