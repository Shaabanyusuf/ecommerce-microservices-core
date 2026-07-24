# E-Commerce Microservices Architecture

A production-grade microservices system built for cloud-native deployment, orchestrated via **Kubernetes** and packaged using **Helm**.

## Architecture Overview

The system consists of two decoupled microservices:
1. **Inventory Service (`inventory-service`)**: Manages products, stock levels, and pricing data (Port: `5001`).
2. **Order Service (`order-service`)**: Handles customer orders and validates stock availability by communicating with the inventory service (Port: `5002`).

## Project Structure

```
├── helm/
│   └── ecommerce-chart/     # Helm chart for deploying the entire architecture
├── inventory-service/       # Inventory microservice source code & dependencies
├── k8s/                     # Raw Kubernetes cluster deployment manifests
│   ├── inventory-deployment.yaml
│   └── order-deployment.yaml
├── order-service/           # Order microservice source code & dependencies
├── Dockerfile.inventory     # Docker image build file for inventory service
├── Dockerfile.order         # Docker image build file for order service
└── README.md                # Project documentation file


```

🚀 ##Deployment Guide using Helm:

To deploy and test these microservices locally inside a Kubernetes cluster (e.g., Minikube or Kind):


1. Build Docker Images inside your cluster:
   docker build -t inventory-service:latest -f Dockerfile.inventory .
   docker build -t order-service:latest -f Dockerfile.order .
2. Deploy the application using Helm:
   helm install ecommerce-release ./helm/ecommerce-chart
3. Verify Deployments, Pods, and Services:
   kubectl get all
4. Uninstall the Release (Cleanup):
   helm uninstall ecommerce-release



---

🚀🚀### Deployment Guide using Cluster:

To deploy and test these microservices directly using raw Kubernetes cluster manifests (without Helm):


1. Build Docker Images inside your local cluster environment:
   docker build -t inventory-service:latest -f Dockerfile.inventory .
   docker build -t order-service:latest -f Dockerfile.order .
2. Apply Kubernetes Manifests for both services:
   kubectl apply -f k8s/inventory-deployment.yaml
   kubectl apply -f k8s/order-deployment.yaml
3. Verify Deployments, Pods, and Services are running successfully:
   kubectl get pods
   kubectl get services
4. Clean up and delete resources when done:
   kubectl delete -f k8s/inventory-deployment.yaml
   kubectl delete -f k8s/order-deployment.yaml

   
