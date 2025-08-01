from fastapi.testclient import TestClient
from assistant.interfaces.web import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post('/chat', json={'user_id': 'u', 'text': 'hello'})
    assert response.status_code == 200
    assert 'reply' in response.json()
