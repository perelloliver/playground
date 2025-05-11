from pydantic import BaseModel

class RequestInput(BaseModel):
    input: str

class RequestOutput(BaseModel):
    label: str
    score: float
    input: str