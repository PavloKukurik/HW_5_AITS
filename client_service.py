import requests
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

APP_TOKEN = "YourSuperSecretToken"

@app.get("/some-protected-route")
def protected_route(authorization: str = Header(None)):
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "You are authorized!"}

@app.get("/process-and-save/{key}")
def process_and_save(key: str, authorization: str = Header(None)):
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    db_url = f"http://localhost:8001/get/{key}"
    db_response = requests.get(db_url)
    db_data = db_response.json()

    if db_data.get("status") == "error":
        return db_data

    process_url = "http://localhost:8002/process"
    process_response = requests.post(process_url, json={"payload": db_data["data"]})
    processed_data = process_response.json()

    save_url = "http://localhost:8001/save"
    requests.post(save_url, json={"key": key, "value": processed_data})

    return {"status": "success", "processed_data": processed_data}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Client Service is up and running."}
