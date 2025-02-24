from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_users():
    """
    Vérifie que la récupération de tous les utilisateurs renvoie une liste (qui peut être vide).
    """
    response = client.get("/users")
    assert response.status_code == 200
    # La réponse doit être une liste (même vide)
    assert isinstance(response.json(), list)


def test_get_user_by_id_not_found():
    """
    Vérifie que la requête d'un utilisateur inexistant renvoie une erreur 404.
    """
    response = client.get("/users/9999")
    assert response.status_code == 404


def test_create_user():
    """
    Vérifie la création d'un nouvel utilisateur.
    """
    user_data = {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "secret"
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 200
    # La réponse doit contenir les données de l'utilisateur créé
    assert response.json() == user_data


def test_get_user_by_id():
    """
    Vérifie la récupération d'un utilisateur existant par son ID.
    """
    # On crée d'abord un utilisateur
    user_data = {
        "id": 2,
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "password": "password123"
    }
    client.post("/users", json=user_data)
    response = client.get("/users/2")
    assert response.status_code == 200
    assert response.json() == user_data


def test_update_user():
    """
    Vérifie la mise à jour des informations d'un utilisateur existant.
    """
    # Création initiale d'un utilisateur
    user_data = {
        "id": 3,
        "name": "Alice",
        "email": "alice@example.com",
        "password": "alicepwd"
    }
    client.post("/users", json=user_data)

    # Données de mise à jour
    updated_data = {
        "id": 3,
        "name": "Alice Cooper",
        "email": "alice.cooper@example.com",
        "password": "newalicepwd"
    }
    response = client.put("/users/3", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data


def test_delete_user():
    """
    Vérifie la suppression d'un utilisateur.
    """
    # Création d'un utilisateur à supprimer
    user_data = {
        "id": 4,
        "name": "Bob",
        "email": "bob@example.com",
        "password": "bobpwd"
    }
    client.post("/users", json=user_data)

    # Suppression de l'utilisateur
    response = client.delete("/users/4")
    assert response.status_code == 200
    # Vérification que l'utilisateur n'existe plus
    response = client.get("/users/4")
    assert response.status_code == 404
