# E-Commerce Microservices Architecture

A production-grade microservices system built for cloud-native deployment, orchestrated via **Kubernetes** and packaged using **Helm**.

## Architecture Overview

The system consists of two decoupled microservices:
1. **Inventory Service (`inventory-service`)**: Manages products, stock levels, and pricing data (Port: `5001`).
2. **Order Service (`order-service`)**: Handles customer orders and validates stock availability by communicating with the inventory service (Port: `5002`).

## Project Structure

```
├── inventory-service/       # Inventory microservice source code & dependencies
├── order-service/           # Order microservice source code & dependencies
├── helm/
│   └── ecommerce-chart/     # Helm chart for deploying the entire architecture
├── Dockerfile.inventory     # Docker image build file for inventory service
└── Dockerfile.order         # Docker image build file for order service
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
