import uvicorn

from fastapi import FastAPI, Depends, HTTPException
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

# Definir el modelo de datos para obtener todos los usuarios (GET)
@app.get("/get_users", response_model=list[UserRead])
def get_users(db: Session = Depends(get_session)):
    users = db.query(User).all()
    return users

# Definir el modelo de datos para crear un usuario (POST)
@app.post("/create_user", response_model=UserRead)
def create_user(payload: UserCreate, db: Session = Depends(get_session)):
    new_user = User(name=payload.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Definir el modelo de datos para borrar un usuario (DELETE)
@app.delete("/delete_user_id")
def delete_user(user_id: int, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()     
    return None


# Inicializar la base de datos y correr el servidor
if __name__ == "__main__":
    init_db()
    with SessionLocal() as session:
        # Acá creamos un usuario nuevo, y lo guardamos en la DB.
        user_new = User(name="Andy")
        session.add(user_new)
        session.commit()

        # Acá obtenemos todos los usuarios dentro de la DB y los mostramos.
        users = session.query(User).all()
        for user in users:
            print("--")
            print(type(user))
            print(user)
            print(user.name)
            print("--")