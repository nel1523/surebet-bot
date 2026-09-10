import os
import requests
import time

TOKEN = os.environ["TELEGRAM_TOKEN"]
URL = f"https://api.telegram.org/bot{TOKEN}"

print("Bot iniciado")

offset = None

while True:
    try:
        respuesta = requests.get(
            f"{URL}/getUpdates",
            params={"timeout": 5, "offset": offset},
            timeout=10
        )

        datos = respuesta.json()

        for update in datos.get("result", []):
            offset = update["update_id"] + 1

            mensaje = update.get("message")
            if not mensaje:
                continue

            chat_id = mensaje["chat"]["id"]
            texto = mensaje.get("text", "")

            if texto == "/start":
                requests.post(
                    f"{URL}/sendMessage",
                    data={
                        "chat_id": chat_id,
                        "text": "🤖 ¡Bot Surebet conectado!\n\nTelegram funciona correctamente."
                    }
                )

        time.sleep(1)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
