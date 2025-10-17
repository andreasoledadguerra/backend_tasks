
from fastapi import Depends
from sqlalchemy.orm import Session
from db import get_session
from requests import UserCreate, UserRead
from models import User


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

