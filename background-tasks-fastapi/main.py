from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import asyncio
import time

app = FastAPI()

class EmailMessage(BaseModel):
    email: str
    message: str

def send_email(email: str, message: str):
    print(f"Sending email to {email}: {message}")
    time.sleep(5)  

@app.post("/send-email/")
async def send_email_background(email_message: EmailMessage, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email_message.email, email_message.message)
    await asyncio.sleep(6)
    return {"message": "Email will be sent in the background. Please wait."}

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI background tasks example"}
