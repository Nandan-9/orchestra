from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("OPENROUTER_KEY")
# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Create chat completion

def chat_completion(chat):
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528:free",
        messages=[
            {
                "role": "user",
                "content": chat,
            }
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

# Print the response

