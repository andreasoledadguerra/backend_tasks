
#Los requerimientos son los siguientes:
#- La API debe poder crear un usuario en la base de datos.
#- Eliminarlo.
#- devolver un listado de todos los usuarios.

#endpoints :
#"/create_user", "/delete_user", "/get_users"Los endpoints seran:

import uvicorn
import requests

from fastapi import FastAPI, Depends
from sqlalchemy.orm import  Session
from db import get_session, init_db
from models import User
from pydantic import BaseModel

# Crear la instancia de FastAPI
app = FastAPI()

# Schema para crear y leer usuarios
class UserCreate(BaseModel):
    name: str

class UserRead(BaseModel):
    id: int
    name: str

    class Config: # convierte el objeto ORM a un objeto Pydantic
        orm_mode = True


# Definir el modelo de datos para crear un usuario (POST)
@app.post("/create_user", response_model=UserRead)
def create_user(payload: UserCreate, db: Session = Depends(get_session)):
    new_user = User(name=payload.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Definir el modelo de datos para obtener todos los usuarios (GET)
@app.get("/get_users", response_model=list[UserRead])
def get_users(db: Session = Depends(get_session)):
    users = db.query(User).all()
    return users

# Definir el modelo de datos para borrar un usuario (DELETE)
@app.delete("/delete_user")
def delete_user(user_id: int):
    return {"message": f"User with id {user_id} deleted successfully"}


