from fastapi import FastAPI
from app.api.routers import items,ai,logs
def create_app()->FastAPI:
    app=FastAPI(title="AI Automation API",version="2.0.0")
    app.include_router(items.router,prefix="/items",tags=["Items"])
    app.include_router(ai.router,prefix="/ai",tags=["AI"])
    app.include_router(logs.router,prefix="/logs",tags=["Logs"])
    return app
app=create_app()
