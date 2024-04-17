from pydantic import BaseModel

class JWTModel(BaseModel):
    signature: str
    msg : str