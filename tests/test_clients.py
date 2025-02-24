from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_client():
    client_data = {"id": 1, "name": "Client One", "email": "client1@example.com"}
    response = client.post("/clients/", json=client_data)
    assert response.status_code == 200
    assert response.json() == client_data

def test_get_clients():
    response = client.get("/clients/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_client():
    client_data = {"id": 2, "name": "Client Two", "email": "client2@example.com"}
    client.post("/clients/", json=client_data)
    response = client.get("/clients/2")
    assert response.status_code == 200
    assert response.json() == client_data

def test_update_client():
    client_data = {"id": 3, "name": "Old Client", "email": "old@example.com"}
    client.post("/clients/", json=client_data)
    updated_data = {"id": 3, "name": "Updated Client", "email": "updated@example.com"}
    response = client.put("/clients/3", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data

def test_delete_client():
    client_data = {"id": 4, "name": "Client to Delete", "email": "delete@example.com"}
    client.post("/clients/", json=client_data)
    response = client.delete("/clients/4")
    assert response.status_code == 200
    # Vérification que le client a bien été supprimé
    response = client.get("/clients/4")
    assert response.status_code == 404
