import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]

respuesta = requests.get(
    f"https://api.telegram.org/bot{TOKEN}/getMe",
    timeout=10
)

print(respuesta.json())
