from pydantic import BaseModel

# Schema para crear y leer usuarios
class UserCreate(BaseModel):
    name: str
    
class UserRead(BaseModel):
    id: int
    name: str
