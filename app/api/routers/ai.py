from fastapi import APIRouter,HTTPException
from app.models.ai import TextRequest
from app.services.ai_service import AIService

router=APIRouter()

@router.post("/task")
def ai_task(req:TextRequest):
    try:
        return AIService.run_task(req.task,req.text)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
