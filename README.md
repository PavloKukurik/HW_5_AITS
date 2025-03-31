# Homework #2 - Basic REST Application with Token Authentication

## Purpose

The goal of this assignment is to create a microservice-based application with token authentication that allows clients to interact securely with the Client Service.

## Microservices Architecture

### 1. Business Logic Service

- `/process`: The core endpoint for processing data (e.g., data transformation, ML inference).
- `/health`: Returns service status (e.g., `{ "status": "ok" }`).
- Root (`/`): Returns a short description of the service.

### 2. Database Service

- `/save`: Endpoint for saving data (using an in-memory database simulation).
- `/get/{key}`: Endpoint for retrieving data by key.
- `/health`: Returns service status.
- Root (`/`): Returns a short description of the service.

### 3. Client Service

- `/process-and-save/{key}`: Orchestrates the process, including reading data from the Database Service, invoking the Business Logic Service, and saving the result back to the Database Service.
- `/health`: Returns service status.
- Root (`/`): Returns a short description of the service.

## Token Authentication

The Client Service requires a token for authentication. The token is verified from the request header `Authorization`. Example of a valid request:

```bash
    curl -X GET "http://localhost:8000/process-and-save/test" -H "Authorization: Bearer SuperSecretToken"
```

## Running the Services

The application uses Docker Compose to run all services together. Ensure Docker is installed and running on your machine.

### Steps to Run:

1. Clone the repository:

```bash
git clone https://github.com/PavloKukurik/HW_5_AITS
cd HW_5_AITS
```

2. Build and run the services using Docker Compose:

```bash
./run.sh
```

Or manually:

```bash
    docker build -t my_microservices .
    docker run -p 8000:8000 -p 8001:8001 -p 8002:8002 my_microservices
```

## Checking Services Health

Verify each service by accessing the following endpoints:

- Client Service: `http://localhost:8000/health`
- Database Service: `http://localhost:8001/health`
- Business Logic Service: `http://localhost:8002/health`

Expected response: `{ "status": "ok" }`

## Example Usage

### Saving Data to Database Service:

```bash
    curl -X POST "http://localhost:8001/save" -H "Content-Type: application/json" -d '{"key": "test", "value": "hello"}'
```

### Processing and Saving Data:

```bash
    curl -X GET "http://localhost:8000/process-and-save/test" -H "Authorization: Bearer SuperSecretToken"
```

### Retrieving Data:

```bash
    curl -X GET "http://localhost:8001/get/test"
```
