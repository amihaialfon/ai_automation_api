from pydantic import BaseSettings
class Settings(BaseSettings):
    base_url:str="http://localhost:8000"
    hf_token:str|None=None
    log_file:str="log.txt"
    class Config:
        env_file=".env"
settings=Settings()
