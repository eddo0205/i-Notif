import requests
import os

# Ambil data dari Secrets
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

def check_notif():
    # Ganti sesuai logika cek notif lu
    notif = True  # contoh: selalu ada notif
    if notif:
        send_telegram("Ada notifikasi baru!")

if __name__ == "__main__":
    check_notif()
