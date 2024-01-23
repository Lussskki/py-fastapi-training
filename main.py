from fastapi import FastAPI, status, HTTPException


app = FastAPI()

tasks = [
    {"id": 1, "Title": "The Dark Knight"},
    {"id": 2, "Title": "The Watchmen"},
    {"id": 3, "Title": "The Vendetta"}
]

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
