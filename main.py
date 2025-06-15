from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sample API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data model
class Item(BaseModel):
    id: int
    name: str
    description: str

# Sample data
items = [
    Item(id=1, name="Item 1", description="This is item 1"),
    Item(id=2, name="Item 2", description="This is item 2"),
    Item(id=3, name="Item 3", description="This is item 3"),
]

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

@app.get("/items", response_model=List[Item])
async def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"} 