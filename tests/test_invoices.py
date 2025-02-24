from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_invoice():
    invoice = {"id": 1, "product_ids": [1, 2], "total": 100.0}
    response = client.post("/invoices/", json=invoice)
    assert response.status_code == 200
    assert response.json() == invoice

def test_get_invoices():
    response = client.get("/invoices/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_invoice():
    invoice = {"id": 2, "product_ids": [2, 3], "total": 150.0}
    client.post("/invoices/", json=invoice)
    response = client.get("/invoices/2")
    assert response.status_code == 200
    assert response.json() == invoice

def test_update_invoice():
    invoice = {"id": 3, "product_ids": [1], "total": 50.0}
    client.post("/invoices/", json=invoice)
    updated_invoice = {"id": 3, "product_ids": [1, 2], "total": 80.0}
    response = client.put("/invoices/3", json=updated_invoice)
    assert response.status_code == 200
    assert response.json() == updated_invoice

def test_delete_invoice():
    invoice = {"id": 4, "product_ids": [3], "total": 60.0}
    client.post("/invoices/", json=invoice)
    response = client.delete("/invoices/4")
    assert response.status_code == 200
    # Vérification que la facture est supprimée
    response = client.get("/invoices/4")
    assert response.status_code == 404
