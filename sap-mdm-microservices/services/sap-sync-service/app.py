import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SAP Synchronization Service")
SAP_BASE_URL = os.getenv('SAP_BASE_URL', 'https://example.sap.system')


class SyncRequest(BaseModel):
    object_type: str
    object_id: str


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@app.post('/sync')
def sync_to_sap(payload: SyncRequest) -> dict[str, str]:
    return {
        'message': 'Sync request accepted',
        'sap_target': SAP_BASE_URL,
        'object_type': payload.object_type,
        'object_id': payload.object_id,
    }
