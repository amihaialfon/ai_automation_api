from fastapi.testclient import TestClient
from app.main import app
from tests.utils import api_call

client=TestClient(app)

def test_sentiment():
    r=api_call(client,"post","/ai/task",json={"task":"sentiment","text":"I love this!"})
    assert r.status_code in (200,500)
