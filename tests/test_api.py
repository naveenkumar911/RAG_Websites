from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_index_endpoint():
    response = client.post("/api/v1/index", json={"url": ["https://example.com"]})
    assert response.status_code == 200
    assert "indexed_url" in response.json()

def test_chat_endpoint():
    response = client.post("/api/v1/chat", json={
        "messages": [{"content": "What is late interaction?", "role": "user"}]
    })
    assert response.status_code == 200
    assert "response" in response.json()
    assert "citation" in response.json()
