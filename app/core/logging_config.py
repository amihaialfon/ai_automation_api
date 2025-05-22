import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from app.core.config import settings

def setup_logging():
    logger=logging.getLogger("ai_automation_api")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        Path(settings.log_file).touch(exist_ok=True)
        handler=RotatingFileHandler(settings.log_file,maxBytes=1_000_000,backupCount=3)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(handler)
    return logger

logger=setup_logging()
