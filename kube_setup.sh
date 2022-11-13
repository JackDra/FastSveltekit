kubectl apply -f sveltekit_frontend/kube/deployment.yaml
kubectl apply -f sveltekit_frontend/kube/service.yaml
kubectl apply -f python_backend/kube/deployment.yaml
kubectl apply -f python_backend/kube/service.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.6.1/aio/deploy/recommended.yaml
kubectl apply -f dashboard_adminuser.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.4.0/deploy/static/provider/cloud/deploy.yaml
kubectl apply -f ingress.yaml
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 80:80