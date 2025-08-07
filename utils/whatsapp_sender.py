import os
import requests

GUPSHUP_API_KEY = os.getenv("GUPSHUP_API_KEY")
SENDER_ID = os.getenv("GUPSHUP_SENDER_ID")

def send_whatsapp_message(phone_number, message):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    payload = {
        "channel": "whatsapp",
        "source": SENDER_ID,
        "destination": phone_number,
        "message": message,
        "src.name": "wellness_whispers"
    }
    headers = {
        "apikey": GUPSHUP_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.status_code == 202
