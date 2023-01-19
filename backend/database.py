from gc import collect
from turtle import title
from unittest import result
from model import Todo

# MongoDB driver
import motor.motor_asyncio

# For the connection between database.py and MongoDB 
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

# Create database called `TodoList`
database = client.TodoList

# Create a collection called `todo` inside the db
# hint: a coolection is the same as a SQL table
collection = database.todo

#########################
### DB Functions
#########################

# Fetch a todo by its title from the db
async def fetch_one_todo(title): 
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos(): 
    todos = list()
    cursor = collection.find({})
    async for document in cursor: 
        todos.append(Todo(**document))
    return todos

async def create_todo(todo): 
    document = todo
    # await for teh collection to insert the document into the collection 
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc): 
    await collection.update_one({"title": title}, {"$set":{"description": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title): 
    await collection.delete_one({"title": title})
    return True
    

    

    

