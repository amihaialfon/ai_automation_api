from pathlib import Path
from typing import List
from app.core.config import settings
def read_logs(lines:int=100)->List[str]:
    p=Path(settings.log_file)
    if not p.exists():
        return []
    return p.open().readlines()[-lines:]
