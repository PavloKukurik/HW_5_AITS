import uvicorn
import multiprocessing
from db_service import app as db_app
from business_service import app as business_app
from client_service import app as client_app

def run_db_service():
    uvicorn.run(db_app, host="0.0.0.0", port=8001)

def run_business_service():
    uvicorn.run(business_app, host="0.0.0.0", port=8002)

def run_client_service():
    uvicorn.run(client_app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=run_db_service),
        multiprocessing.Process(target=run_business_service),
        multiprocessing.Process(target=run_client_service),
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
