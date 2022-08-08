docker build . --tag svelte_frontend
docker run -p 3000:3000 --network=fastsvelte_network --name svelte_frontend svelte_frontend