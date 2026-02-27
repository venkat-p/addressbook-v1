import os
from typing import Any, Dict

import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="sap-sync-service", version="1.0.0")

SAP_BASE_URL = os.getenv("SAP_BASE_URL", "https://sandbox.api.sap.com/s4hanacloud")
SAP_API_KEY = os.getenv("SAP_API_KEY", "")
SAP_CUSTOMER_API_PATH = os.getenv(
    "SAP_CUSTOMER_API_PATH",
    "/sap/opu/odata/sap/API_BUSINESS_PARTNER/A_BusinessPartner",
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/sync/customers")
def sync_customers() -> Dict[str, Any]:
    if not SAP_API_KEY:
        raise HTTPException(
            status_code=400,
            detail="SAP_API_KEY environment variable is not set",
        )

    endpoint = f"{SAP_BASE_URL.rstrip('/')}{SAP_CUSTOMER_API_PATH}"
    response = requests.get(
        endpoint,
        headers={"APIKey": SAP_API_KEY, "Accept": "application/json"},
        params={"$top": 10, "$format": "json"},
        timeout=20,
    )

    if response.status_code >= 400:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    payload = response.json()
    records = payload.get("d", {}).get("results", [])
    return {"synced_records": len(records), "source": endpoint}
