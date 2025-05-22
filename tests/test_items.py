from fastapi.testclient import TestClient
from app.main import app
from tests.utils import api_call

client=TestClient(app)

def test_lifecycle():
    r=api_call(client,"post","/items/",json={"name":"Mouse"})
    assert r.status_code==200
    iid=r.json()["id"]
    assert api_call(client,"get",f"/items/{iid}").status_code==200
    assert api_call(client,"put",f"/items/{iid}",json={"name":"Mouse2"}).status_code==200
    assert api_call(client,"delete",f"/items/{iid}").status_code==200
