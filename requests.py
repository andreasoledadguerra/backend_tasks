from pydantic import BaseModel

# Schema para crear y leer usuarios
class UserCreate(BaseModel):
    name: str
    
class UserRead(BaseModel):
    id: int
    name: str

    class Config: # convierte el objeto ORM a un objeto Pydantic
        orm_mode = True
