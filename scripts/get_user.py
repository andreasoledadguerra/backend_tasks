from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_session
from requests import UserRead
from models import User

#@app.get("/get_users", response_model=list[UserRead])
def get_user(db: Session = Depends(get_session)) -> list[UserRead]:
    users = db.query(User).all()
    return users