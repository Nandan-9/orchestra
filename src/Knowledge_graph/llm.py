import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY missing")

URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}

def chat_completion(messages, model="arcee-ai/trinity-large-preview:free", temperature=0):
    response = requests.post(
        URL,
        headers=HEADERS,
        json={
            "model": model,
            "messages": messages,
            "temperature": temperature
        }
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]