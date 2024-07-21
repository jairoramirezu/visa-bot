import os
from dotenv import load_dotenv
import httpx

load_dotenv()


async def send_message(msg):
    url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"
    payload = {
        'chat_id': os.getenv('CHAT_ID'),
        'text': msg
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=payload)
        response.raise_for_status()
