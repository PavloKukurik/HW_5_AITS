docker build -t my_microservices .

docker run -p 8000:8000 -p 8001:8001 -p 8002:8002 my_microservices