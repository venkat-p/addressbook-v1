# SAP Master Data Management (MDM) Microservices on Kubernetes

This package provides starter code for a microservices-based Master Data Management solution designed for SAP integration and Kubernetes deployment.

## Included microservices

- **business-partner-service**: CRUD-style API for business partner master records.
- **material-service**: CRUD-style API for material master records.
- **sap-sync-service**: API to trigger synchronization events to SAP.

Each service is implemented using FastAPI and can be containerized with the provided Dockerfile.

## Project structure

```text
sap-mdm-microservices/
  services/
    business-partner-service/
    material-service/
    sap-sync-service/
  k8s/
    namespace.yaml
    business-partner.yaml
    material.yaml
    sap-sync.yaml
    ingress.yaml
```

## Run locally (per service)

```bash
cd services/business-partner-service
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8080
```

Repeat for the other services.

## Build container images

```bash
docker build -t ghcr.io/your-org/business-partner-service:latest services/business-partner-service
docker build -t ghcr.io/your-org/material-service:latest services/material-service
docker build -t ghcr.io/your-org/sap-sync-service:latest services/sap-sync-service
```

## Deploy to Kubernetes

Update image names in the manifests if needed, then apply:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/business-partner.yaml
kubectl apply -f k8s/material.yaml
kubectl apply -f k8s/sap-sync.yaml
kubectl apply -f k8s/ingress.yaml
```

## Notes for SAP integration

- Set real SAP endpoint and credentials via Kubernetes Secret/ConfigMap.
- Replace mock sync logic in `sap-sync-service` with RFC/OData/BAPI client calls.
- Add authentication/authorization (OAuth2/JWT) and API gateway policy controls before production use.
