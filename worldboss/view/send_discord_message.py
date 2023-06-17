import requests
import json

def send_discord_message(webhook_url, content):
    data = {
        "content": content
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    
    if response.status_code == 204:
        print("Message sent successfully to Discord channel!")
    else:
        print(f"Failed to send message to Discord channel. Error: {response.status_code}")
