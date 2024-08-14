import requests
from dotenv import load_dotenv
import os
# Define the URL for the Bland AI API endpoint
load_dotenv()
url = "https://api.bland.ai/v1/calls"
api_key= os.environ.get("API_KEY")
# Define the payload with all the necessary parameters for the API request
payload = {
    "phone_number": "+19797393588",  # The phone number to which the call will be made
    "task": "Remind the Customer about their appointment",  # Description of the task
    "voice": "maya",  # Voice to be used for the call
    "first_sentence": "Hello! This is a reminder about your appointment.",  # First sentence to be spoken in the call
    "wait_for_greeting": True,  # Whether to wait for a greeting before proceeding
    "block_interruptions": False,  # Whether to block interruptions during the call
    "interruption_threshold": 123,  # Threshold for handling interruptions
    "model": "enhanced",  # Model to be used for the call
    "temperature": 0.7,  # Temperature setting for the AI model
    "keywords": ["reminder", "appointment"],  # Keywords related to the call
    "pronunciation_guide": [{}],  # Pronunciation guide for specific words
    "transfer_phone_number": "+15512008317",  # Phone number to transfer the call to, if needed
    "transfer_list": {"default": "+15512008317"},  # List of phone numbers for call transfer
    "language": "en-US",  # Language for the call
    "calendly": {},  # Placeholder for Calendly integration
    "timezone": "America/New_York",  # Timezone setting for the call
    "request_data": {},  # Additional request data
    "voicemail_message": "Hello, this is a test message",  # Message to be left if the call goes to voicemail
    "voicemail_action": "leave_message",  # Action to take if the call goes to voicemail
    "retry": {
        "wait": 10,  # Wait time before retrying the call
        "voicemail_action": "leave_message",  # Action to take if the retry goes to voicemail
        "voicemail_message": "Hello, this is a test message."  # Message for voicemail on retry
    },
    "max_duration": 30,  # Maximum duration of the call in seconds
    "record": True,  # Whether to record the call
    "webhook": "https://bland-ai-431701.ts.r.appspot.com/webhook",  # Webhook URL to receive call data
    "metadata": {},  # Additional metadata for the call
    "summary_prompt": "Summarize the call with 'See you, have a good one'",  # Prompt to summarize the call
    "answered_by_enabled": True  # Whether to enable answered-by detection
}

# Define the headers with authorization and content type
headers = {
    "authorization": api_key,  # API key for authorization
    "Content-Type": "application/json"  # Content type for the request
}

# Make the POST request to the Bland AI API with the defined URL, payload, and headers
response = requests.post(url, json=payload, headers=headers)

# Print the response from the API
print(response.text)