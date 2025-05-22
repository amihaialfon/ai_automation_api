from fastapi import APIRouter
from app.services.log_service import read_logs
router=APIRouter()
@router.get("/")
def logs(lines:int=100):
    return read_logs(lines)
