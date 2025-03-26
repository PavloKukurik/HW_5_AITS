import time
from fastapi import FastAPI

app = FastAPI()

@app.post("/process")
def process_data(payload: dict):
    time.sleep(2)  # Симуляція довгої обробки
    processed_result = {"original": payload, "processed": True}
    return processed_result

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Business Logic Service is up and running."}
