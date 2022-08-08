docker build . --tag jackdra90/fastapi_backend
docker run -p 8000:8000 --network=fastsvelte_network --name fastapi_backend jackdra90/svelte_frontend