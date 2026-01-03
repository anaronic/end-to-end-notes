from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import os

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["hackathon"]
notes = db["notes"]

class Note(BaseModel):
    text: str

@app.post("/add")
def add_note(note: Note):
    notes.insert_one(note.dict())
    return {"message": "Note added"}

@app.get("/all")
def get_notes():
    return {"notes": [n["text"] for n in notes.find()]}
