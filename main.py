from fastapi import FastAPI
from pydantic import BaseModel
import json
import uvicorn

app = FastAPI()



class Item(BaseModel):
    product_name: str
    description: str = None,
    price: float
    tex: float = None




@app.post("/create_request/")
async def create_request(item:Item):
                print("Received item data:")
                print(item.json())
                try:      
                    with open("db/database.json", "a") as json_file:
                            json.dump(item.dict(), json_file, ensure_ascii=False, indent=4)    
                            json_file.write(",")
                except Exception as e:
                        print(f"Error writing to file: {e}")            
                return item

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