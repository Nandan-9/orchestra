import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

url = "https://openrouter.ai/api/v1/chat/completions"

# -----------------------
# First API Call
# -----------------------
response1 = requests.post(
    url,
    headers=headers,
    json={
        "model": "arcee-ai/trinity-large-preview:free",
        "messages": [
            {
                "role": "user",
                "content": "How many r's are in the word 'strawberry'?"
            }
        ],
        "reasoning": {"enabled": True}
    }
)

response1.raise_for_status()
data1 = response1.json()

assistant_message = data1["choices"][0]["message"]

# -----------------------
# Preserve conversation
# -----------------------
messages = [
    {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
    {
        "role": "assistant",
        "content": assistant_message.get("content"),
        "reasoning_details": assistant_message.get("reasoning_details")
    },
    {"role": "user", "content": "Are you sure? Think carefully."}
]

# -----------------------
# Second API Call
# -----------------------
response2 = requests.post(
    url,
    headers=headers,
    json={
        "model": "arcee-ai/trinity-large-preview:free",
        "messages": messages,
        "reasoning": {"enabled": True}
    }
)

response2.raise_for_status()
data2 = response2.json()

print("Final Response:")
print(data2["choices"][0]["message"]["content"])