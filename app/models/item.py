from pydantic import BaseModel,Field
from typing import Optional
class Item(BaseModel):
    name:str=Field(...,example="Keyboard")
    description:Optional[str]=Field(None,example="Mechanical keyboard")
