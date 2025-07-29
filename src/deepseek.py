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
completion = client.chat.completions.create(
    model="deepseek/deepseek-chat",
    messages=[
        {"role": "user",
         "content":
             "Create a Manim animation that shows a sine wave growing from a unit circle."
         }
    ]
)




# Print the response
print(completion.choices[0].message.content)
