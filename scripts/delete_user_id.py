from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import  Session
from db import get_session
from models import User
from pydantic import BaseModel  

app = FastAPI()

@app.delete("/delete_user_id")
def delete_user(user_id: int, db: Session = Depends(get_session))-> None:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()     
    return None