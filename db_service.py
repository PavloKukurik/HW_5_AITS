from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
data_store = {}

class Data(BaseModel):
    key: str
    value: str

@app.post("/save")
def save_data(payload: dict):
    key = payload.get("key")
    value = payload.get("value")
    data_store[key] = value  # Збереження в пам'яті
    return {"status": "success", "message": f"Data with key '{key}' saved."}

@app.get("/get/{key}")
def get_data(key: str):
    if key in data_store:
        return {"status": "success", "data": data_store[key]}
    else:
        return {"status": "error", "message": f"Data with key '{key}' not found."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Database Service is up and running."}
