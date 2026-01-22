from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    qty: int

items: List[Item] = []

@app.get("/")
def root():
    return {"message": "Python API is running 🚀"}

@app.get("/health")
def health():
    return "OK"

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def add_item(item: Item):
    items.append(item)
    return {"status": "saved", "item": item}
