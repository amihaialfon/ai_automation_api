from fastapi.testclient import TestClient
def api_call(c:TestClient,method:str,url:str,**kw):
    return getattr(c,method.lower())(url,**kw)
