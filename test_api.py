from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("OPENROUTER_KEY")
print(f"API Key loaded: {api_key[:20]}..." if api_key else "No API key found")

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Test the API call
try:
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528:free",
        messages=[
            {
                "role": "user",
                "content": "Hello",
            }
        ]
    )
    print("Success!")
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}") 