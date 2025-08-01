from typing import Union

from fastapi import FastAPI,Body
from openai import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.deepseek import chat_completion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",                      # for local development
        "https://your-vercel-deployment.vercel.app"  # for production frontend
    ],  # Allow frontend
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, etc.
    allow_headers=["*"],
)


class User(BaseModel):
    name: str
    age: int
    email: str
@app.get("/")
def read_root():
    return {"Hello": "World"}
class ChatMessage(BaseModel):
    content:str

class UserCreate(BaseModel):
    name: str

@app.post("/create-user/")
def create_user(user: UserCreate):
    print(user.name)
    return {"user_id": 1, "name": user.name}

