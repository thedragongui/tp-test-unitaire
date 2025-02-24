from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Client

router = APIRouter()

# Base de données simulée pour les clients
clients_db: List[Client] = []

@router.post("/", response_model=Client)
def create_client(client: Client):
    clients_db.append(client)
    return client

@router.get("/", response_model=List[Client])
def get_clients():
    return clients_db

@router.get("/{client_id}", response_model=Client)
def get_client(client_id: int):
    for client in clients_db:
        if client.id == client_id:
            return client
    raise HTTPException(status_code=404, detail="Client not found")

@router.put("/{client_id}", response_model=Client)
def update_client(client_id: int, updated_client: Client):
    for index, client in enumerate(clients_db):
        if client.id == client_id:
            clients_db[index] = updated_client
            return updated_client
    raise HTTPException(status_code=404, detail="Client not found")

@router.delete("/{client_id}")
def delete_client(client_id: int):
    for client in clients_db:
        if client.id == client_id:
            clients_db.remove(client)
            return {"message": "Client deleted"}
    raise HTTPException(status_code=404, detail="Client not found")
