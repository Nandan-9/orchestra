from typing import Union

from fastapi import FastAPI
from openai import BaseModel

from src.deepseek import chat_completion

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
class ChatMessage(BaseModel):
    content:str

@app.get("/generate/{chat_id}")
def read_item(chat_id: int, chat: Union[str, None] = None):
    repsonse = chat_completion()
    return