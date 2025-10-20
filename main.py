import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import  Session
from db import get_session, init_db
from models import User
from pydantic import BaseModel
from request import UserCreate, UserRead

#http://127.0.0.1:8000

# Crear la instancia de FastAPI
app = FastAPI()


# Inicializar la base de datos al iniciar la aplicación
@app.get("/")
def read_root():
    return {"message": "API funcionando. Ir a /docs para ver endpoints."}

# Definir el modelo de datos para obtener todos los usuarios (GET)
@app.get("/get_users", response_model=list[UserRead])
def get_user(db: Session = Depends(get_session)) -> list[UserRead]:
    users = db.query(User).all()
    return users

# Definir el modelo de datos para crear un usuario (POST)
@app.post("/create_user", response_model=UserRead, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_session)) -> UserRead:
    # Crear la instancia ORM con los datos validados por Pydantic
    new_user = User(name=payload.name)

    # Persistir en la DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Devolver el objeto ORM; FastAPI lo serializa usando response_model (orm_mode=True)
    return new_user

# Definir el modelo de datos para borrar un usuario (DELETE)
@app.delete("/delete_user_id")
def delete_user(user_id: int, db: Session = Depends(get_session)) -> None:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()     
    return None

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
