from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List

app = FastAPI(title="master-data-service", version="1.0.0")


class Customer(BaseModel):
    customer_id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    country: str = Field(..., min_length=2, max_length=2)
    email: str


CUSTOMERS: Dict[str, Customer] = {}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/customers", response_model=List[Customer])
def list_customers() -> List[Customer]:
    return list(CUSTOMERS.values())


@app.post("/customers", response_model=Customer)
def create_customer(customer: Customer) -> Customer:
    if customer.customer_id in CUSTOMERS:
        raise HTTPException(status_code=409, detail="customer already exists")
    CUSTOMERS[customer.customer_id] = customer
    return customer


@app.get("/customers/{customer_id}", response_model=Customer)
def get_customer(customer_id: str) -> Customer:
    customer = CUSTOMERS.get(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="customer not found")
    return customer
