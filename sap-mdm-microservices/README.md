# SAP Master Data Management Microservices on Kubernetes

This package adds a **downloadable starter codebase** for a simple Master Data Management (MDM) setup integrated with SAP APIs, built as microservices and ready to run on Kubernetes.

## Included microservices

1. **master-data-service**
   - REST API for managing customer master data.
   - Endpoints:
     - `GET /health`
     - `GET /customers`
     - `POST /customers`
     - `GET /customers/{customer_id}`

2. **sap-sync-service**
   - Calls SAP S/4HANA API (`API_BUSINESS_PARTNER`) to sync customer records.
   - Endpoints:
     - `GET /health`
     - `POST /sync/customers`

## Folder structure

```text
sap-mdm-microservices/
  services/
    master-data-service/
    sap-sync-service/
  k8s/
    namespace.yaml
    master-data-deployment.yaml
    sap-sync-deployment.yaml
    sap-sync-config.yaml
    sap-sync-secrets.example.yaml
    ingress.yaml
```

## Build container images

```bash
cd sap-mdm-microservices/services/master-data-service
docker build -t ghcr.io/your-org/master-data-service:latest .

cd ../sap-sync-service
docker build -t ghcr.io/your-org/sap-sync-service:latest .
```

Push both images to your registry and update image names in Kubernetes manifests if needed.

## Deploy to Kubernetes

```bash
kubectl apply -f sap-mdm-microservices/k8s/namespace.yaml
kubectl apply -f sap-mdm-microservices/k8s/sap-sync-config.yaml
kubectl apply -f sap-mdm-microservices/k8s/sap-sync-secrets.example.yaml
kubectl apply -f sap-mdm-microservices/k8s/master-data-deployment.yaml
kubectl apply -f sap-mdm-microservices/k8s/sap-sync-deployment.yaml
kubectl apply -f sap-mdm-microservices/k8s/ingress.yaml
```

## SAP configuration

Set these values via ConfigMap/Secret:

- `SAP_BASE_URL`
- `SAP_CUSTOMER_API_PATH`
- `SAP_API_KEY`

> Replace the secret in `sap-sync-secrets.example.yaml` before production use.

## Notes

- This is a starter/reference implementation for microservice decomposition and Kubernetes hosting.
- For production, add persistence (PostgreSQL), service mesh, retry/circuit breaker policies, and secure secret management (e.g., External Secrets + Vault).
