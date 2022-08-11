docker login
docker pull jackdra90/svelte_frontend
docker pull jackdra90/fastapi_backend
docker network create fastsvelte_network
nohup docker run -p 8000:8000 --network=fastsvelte_network --name fastapi_backend jackdra90/fastapi_backend > fastapi_backend.out&
nohup docker run -p 3000:3000 --network=fastsvelte_network --name svelte_frontend jackdra90/svelte_frontend > svelte_frontend.out&
