from http.client import responses

from fastapi import FastAPI, APIRouter
from openai import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.rag.manim_prompter import manim_prompter
from src.rag.types import  input_prompt

app = FastAPI()
router = APIRouter()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend
    allow_credentials=True,
    allow_methods=["*"],
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

@app.post("/chat/")
def create_user(chat: input_prompt):
    print(chat.prompt)
    response = manim_prompter(chat.prompt)
    return {"chat": response}