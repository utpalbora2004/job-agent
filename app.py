import requests

TOKEN = "8622743519: AAGErMlJBxTpuzdseFgEhX5dYZXDNbAgrM0"
CHAT_ID = "7289211505"

def send_message(text):
    url = f"https://api.telegram.org/bot8622743519:AAGErMlJBxTpuzdseFgEhX5dYZXDNbAgrM0/sendMessage"
    data = {
        "chat_id": 7289211505,
        "text": text
    }
    respond=requests.post(url, data=data)
    print(respond.text)

if __name__ == "__main__":
    send_message(" Your Job Agent is Working!")
