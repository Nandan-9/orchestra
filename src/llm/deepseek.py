from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("OPENROUTER_API_KEY")
# Initialize OpenAI client# print(api_key)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
# Create chat completion

def chat_completion(chat):
    completion = client.chat.completions.create(
        model="x-ai/grok-4-fast:free",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": chat,
            }
        ]
    )
    return completion.choices[0].message.content

# Print the response

