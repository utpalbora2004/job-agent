import requests
import time
import threading
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

TOKEN = "8622743519:AAGErMlJBxTpuzdseFgEhX5dYZXDNbAgrM0"
CHAT_ID = 7289211505

# ---------------- BOT FUNCTION ----------------
def send_message(text):
    url = f"https://api.telegram.org/bot8622743519:AAGErMlJBxTpuzdseFgEhX5dYZXDNbAgrM0/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

# ---------------- DUMMY SERVER ----------------
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    PORT = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

# ---------------- MAIN ----------------
if __name__ == "__main__":
    # Start server in background thread
    threading.Thread(target=run_server).start()

    # Run your bot loop
    while True:
        send_message("✅ Bot running properly")
        time.sleep(86400)  # 24 hours