from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

def send_email(email: str, message: str):
    # Simulate sending email (replace with actual email sending logic)
    print(f"Sending email to {email}: {message}")
    time.sleep(5)  # Simulate delay

@app.post("/send-email/")
async def send_email_background(email: str, message: str, background_tasks: BackgroundTasks):
    # Enqueue the send_email task to be executed in the background
    background_tasks.add_task(send_email, email, message)
    return {"message": "Email will be sent in the background"}

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI background tasks example"}
