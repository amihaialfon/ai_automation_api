import requests
from app.core.config import settings
from app.core.logging_config import logger

MODEL_MAP={"sentiment":"distilbert-base-uncased-finetuned-sst-2-english",
           "summarization":"facebook/bart-large-cnn"}

class AIService:
    base="https://api-inference.huggingface.co/models/"
    @classmethod
    def run_task(cls,task:str,text:str):
        if task not in MODEL_MAP:
            raise ValueError(f"Unsupported task {task}")
        url=cls.base+MODEL_MAP[task]
        headers={"Authorization":f"Bearer {settings.hf_token}"} if settings.hf_token else {}
        logger.info("AI task %s",task)
        r=requests.post(url,headers=headers,json={"inputs":text})
        logger.info("HF status %s",r.status_code)
        if r.status_code==200:
            return r.json()
        r.raise_for_status()
