import requests
import time

TOKEN = "8622743519: AAGErMlJBxTpuzdseFgEhX5dYZXDNbAgrM0"
CHAT_ID = "7289211505"

def send_message(text):
    url = f"https://api.telegram.org/bot8622743519:AAGErMlJBxTpuzdseFgEhX5dYZXDNbAgrM0/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

if __name__ == "__main__":
    while True:
        send_message("🚀 updated Job Agent is Running...")
        time.sleep(86400)  # 24 hour