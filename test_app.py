from fastapi.testclient import TestClient
from main import app  # Импортируем наше приложение из main.py

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "service" in data
    assert "version" in data

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["books"], list)
    assert len(data["books"]) > 0

def test_get_book_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Мастер и Маргарита"

def test_book_not_found():
    response = client.get("/books/999")
    assert response.status_code == 404