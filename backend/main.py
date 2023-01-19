from urllib import response
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.model import Todo

# App object
app = FastAPI()

from database import (
    create_todo, 
    fetch_all_todos, 
    fetch_one_todo, 
    remove_todo, 
    update_todo
)

# 300 port for React 
origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# test the api
@app.get("/")
def read_root():
    return {"Response": 200}

# get todo 
@app.get("/api/todo")
async def get_todo(): 
    response = await fetch_all_todos()
    return response

# get a todo by its id
@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_id(title): 
    response = fetch_one_todo(title)
    if response: 
        return response
    raise HTTPException(404, f"there is no todo item with this title {title}")

# create a new todo
@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo): 
    response = await create_todo(todo.dict())
    if response: 
        response
    raise HTTPException(400, "something went wrong / bad request")

# update a todo by its id 
@app.put("/api/todo{title}", response_model=Todo)
async def put_todo(title: str, desc: str): 
    response = await update_todo(title, desc)
    if response: 
        return response
    raise HTTPException(404, f"there is no todo item with this title {title}")

# delete a todo by its id 
@app.delete("/api/todo{title}")
async def delete_todo(title): 
    response = await remove_todo(title)
    if response: 
        return "sucessfully delete todo item"
    raise HTTPException(404, f"there is no todo item with this title {title}")