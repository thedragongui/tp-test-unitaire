from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    product = {"id": 1, "name": "Test Product", "price": 12.99}
    response = client.post("/products/", json=product)
    assert response.status_code == 200
    assert response.json() == product

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_product():
    # Création d'un produit spécifique pour le test
    product = {"id": 2, "name": "Another Product", "price": 22.50}
    client.post("/products/", json=product)
    response = client.get("/products/2")
    assert response.status_code == 200
    assert response.json() == product

def test_update_product():
    # Création d'un produit à mettre à jour
    product = {"id": 3, "name": "Old Product", "price": 15.00}
    client.post("/products/", json=product)
    updated_product = {"id": 3, "name": "Updated Product", "price": 20.00}
    response = client.put("/products/3", json=updated_product)
    assert response.status_code == 200
    assert response.json() == updated_product

def test_delete_product():
    # Création d'un produit à supprimer
    product = {"id": 4, "name": "To be deleted", "price": 5.00}
    client.post("/products/", json=product)
    response = client.delete("/products/4")
    assert response.status_code == 200
    # Vérification que le produit n'est plus accessible
    response = client.get("/products/4")
    assert response.status_code == 404
