from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Material Master Service")


class Material(BaseModel):
    material_id: str
    description: str
    base_uom: str


STORE: dict[str, Material] = {}


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@app.post('/materials', response_model=Material)
def upsert_material(payload: Material) -> Material:
    STORE[payload.material_id] = payload
    return payload


@app.get('/materials/{material_id}', response_model=Material)
def get_material(material_id: str) -> Material:
    return STORE[material_id]
