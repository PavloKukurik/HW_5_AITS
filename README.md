# Homework #2 - Development of a Basic REST Application with Token Authentication

## Overview

In this homework, the goal is to create a microservice-based application in Python using FastAPI. The objective is to gain hands-on experience in building a simple application, as a set of such applications would later form a larger solution.

## Requirements

### 1. Microservice Decomposition

- **Business Logic Service**
  - Exposes a core endpoint (e.g., `/process`) to perform the main "long-running" logic, such as ML model inference, data transformations, or any processing that might take a few seconds.
  - Optional: Call an API of a Large Language Model (LLM) for inference (e.g., https://openrouter.ai/).
  - Includes a `/health` endpoint for basic status reporting.
  - The root (`/`) endpoint should return a short description of the service.

- **Database Service**
  - A service that handles reading and writing data.
  - Simulate a database using an in-memory Python structure (e.g., lists, dictionaries).
  - At least two endpoints:
    - One for saving data (e.g., `/save`).
    - One for retrieving data (e.g., `/get`).
  - Includes a `/health` endpoint.
  - The root (`/`) endpoint should return a short description of the service.

- **Client Service**
  - The only service directly accessible by external clients.
  - Orchestrates calls to both the Database Service and the Business Logic Service:
    1. Reads data from the Database Service.
    2. Calls the Business Logic Service to process or transform the data.
    3. Saves the result back to the Database Service.
    4. Returns the final response to the user.
  - Requires token-based authentication for access (via the request header).
  - Includes a `/health` endpoint.
  - The root (`/`) endpoint should return a short description of the service.

### 2. Security Constraint

- The **Client Service** is the only publicly accessible endpoint, apart from the `/health` endpoint. Users should not have direct access to the Database or Business Logic services.
- A minimal token-based authentication mechanism is required. You can define a fixed token in an environment variable or in the code and require it in the "Authorization" header.

### 3. Health Check Endpoints

- Each service must provide a `/health` endpoint that returns a simple JSON status (e.g., `{"status": "ok"}`) for easy verification that each service is running.

### 4. Optional Extensions

- You may split the **Business Logic Service** into multiple sub-services (e.g., one for data preprocessing and another for the ML model). This is optional.
- You can demonstrate asynchronous calls, add Docker support, or create a simple Docker Compose file to run all services together. This is not strictly required but is a great opportunity to learn.

## Deliverables

### 1. Source Code

- Organize the microservices into clearly separated files/modules (e.g., `client_service.py`, `business_service.py`, `db_service.py`).
- Each service must be a small FastAPI application with its respective endpoints.

### 2. README/Documentation

- Provide clear instructions on how to run each service or start them all together.
- Explain how the token-based authentication works for the Client Service.
- Summarize the request flow: Client → (Client Service) → Database Service → Business Logic Service → Database Service → Client.

### 3. Example Usage

- Provide examples of HTTP requests (e.g., using `curl`, Postman, or a Python script) demonstrating how a user can interact with the Client Service endpoint, trigger the orchestration flow, and get the result.
- It would be helpful to provide a script to start the app with one command.
