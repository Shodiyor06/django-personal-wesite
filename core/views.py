from django.http import JsonResponse
from django.conf import settings
import json
import requests


def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)

        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        text = (
            f"📩 Yangi Contact Xabari!\n\n"
            f"👤 Ism: {name}\n"
            f"📧 Email: {email}\n"
            f"✉️ Xabar:\n{message}"
        )

        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

        requests.post(url, json={
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": text
        })

        return JsonResponse({"ok": True, "msg": "Xabar yuborildi"})

    return JsonResponse({"error": "POST method required"}, status=400)
