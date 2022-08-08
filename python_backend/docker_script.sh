docker build . --tag fastapi_backend
docker run -p 8000:8000 --network=fastsvelte_network --name fastapi_backend fastapi_backend