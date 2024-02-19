from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

# Item model
class Item(BaseModel):
    id: Optional[int]
    Quote: str
    Author: str
     
# Function to read data from the file
def read_data_from_file():
    try:
        with open("db/database.json", "r", encoding= "utf-8") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Error decoding JSON: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {e}")

# Function to write data to the file
def write_data_to_file(data):
    try:
        with open("db/database.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error writing to file: {e}")

# GET method to retrieve data from database.json
@app.get("/get_request")
async def get_request():
    data = read_data_from_file()
    return JSONResponse(content=data)

# POST method to add data to database.json
@app.post("/create_request/")
async def create_request(item: Item):
    print("Received item data:")
    print(item.json())
    data = read_data_from_file()
    data.append(item.dict())
    write_data_to_file(data)
    return item
# PUT method to update your exciting data
@app.put("/put_request/{item_id}")
async def put_request(item_id: int, item: Item):
    print("Updated item data:")
    print(item.dict())  
    data = read_data_from_file()
    data[item_id] = item.dict()  
    write_data_to_file(data)
    return item
# Delete method 
@app.delete("/delete_request/{item_id}")
async def delete_request(item_id: int):
    data = read_data_from_file()
    for item in data:
        if item.get("id") == item_id:
            data.remove(item)
            write_data_to_file(data)
            return {"message": f"Item with ID {item_id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)





"""" 
if i need this code i will look it, it's for me      
 import os 
 import json
 from fastapi import FastAPI, status, HTTPException
 app = FastAPI() tasks = [
         {"id": 1, "Title": "The Dark Knight"},
         {"id": 2, "Title": "The Watchmen"},
         {"id": 3, "Title": "The Vendetta"},
         {"id": 4, "Title": "Spider man"}
         ]
 # print(tasks)

    
 @app.get("/")
 def home():
     return tasks

 @app.get("/ty1/{task_id}")
 def v1(task_id: int):
     result = {}
     for task in tasks:
         if task["id"] == task_id:
             result = task
             return result

     if result == {}:
         raise HTTPException(status_code=404, detail=status.HTTP_404_NOT_FOUND)
     else:
         return result

 @app.post("/ty1/{task_id}")
 def create_task(task_id: int,task:dict):
     new_task_id = max(task["id"] for task in tasks) + 1
     task["id"] = task_id
     tasks.append(task)
     print("Received task:", task)
     print("Updated tasks list:", tasks)
     return tasks 
"""