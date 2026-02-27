from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Business Partner Master Service")


class BusinessPartner(BaseModel):
    partner_id: str
    name: str
    country: str


STORE: dict[str, BusinessPartner] = {}


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@app.post('/business-partners', response_model=BusinessPartner)
def upsert_business_partner(payload: BusinessPartner) -> BusinessPartner:
    STORE[payload.partner_id] = payload
    return payload


@app.get('/business-partners/{partner_id}', response_model=BusinessPartner)
def get_business_partner(partner_id: str) -> BusinessPartner:
    return STORE[partner_id]
