docker build . --tag jackdra90/svelte_frontend
docker run -p 3000:3000 --network=fastsvelte_network --name svelte_frontend jackdra90/svelte_frontend