import os 
import json
from fastapi import FastAPI, status, HTTPException


app = FastAPI()

# db folder
db_folder = "db"

tasks_file = os.path.join(db_folder, "tasks.json")

# Load existing tasks from JSON file if it exists
if os.path.exists(tasks_file):
    with open(tasks_file, "r") as file:
        tasks = json.load(file)
else:
    tasks = [
        {"id": 1, "Title": "The Dark Knight"},
        {"id": 2, "Title": "The Watchmen"},
        {"id": 3, "Title": "The Vendetta"}
    ]

    
print(tasks)
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