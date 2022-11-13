kubectl apply -f sveltekit_frontend/kube/deployment.yaml
kubectl apply -f sveltekit_frontend/kube/service.yaml
kubectl apply -f python_backend/kube/deployment.yaml
kubectl apply -f python_backend/kube/service.yaml