from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import os

app = FastAPI()

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
