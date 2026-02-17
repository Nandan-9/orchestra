import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class ChatOpenRouter(ChatOpenAI):
    def __init__(self, **kwargs):
        super().__init__(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            **kwargs
        )

openrouter_model = ChatOpenRouter(
    model="arcee-ai/trinity-large-preview:free",
    temperature=0
)