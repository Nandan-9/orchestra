from http.client import responses
from fastapi import BackgroundTasks
from fastapi import FastAPI, APIRouter
from openai import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.manim.code_extractor import extractor
from src.manim.code_validation import validate_python_code
from src.manim.render import save_code, render_manim_scene
from src.rag.manim_prompter import manim_prompter
from src.rag.types import  input_prompt
import requests
import uuid
url = "http://127.0.0.1:8001/render"
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
async def generate_prompt(chat: input_prompt, background_tasks: BackgroundTasks):
    print(chat.prompt)



    # 1. Get Manim code from LLM
    responses = manim_prompter(chat.prompt)
    code =  extractor(responses)
    payload = {"code": code}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Video URL:", data["url"])
        return {"url": data["url"]}
    else:
        print("Error:", response.status_code, response.text)
        return {"error": response.status_code}

    # # 2. Save it to a .py file


    # # 3. Render in background
    #
    # # 4. Return the video pat63h
