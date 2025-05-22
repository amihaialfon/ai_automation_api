from pydantic import BaseModel,Field
class TextRequest(BaseModel):
    task:str=Field("sentiment",example="sentiment")
    text:str=Field(...,example="I love this product!")
