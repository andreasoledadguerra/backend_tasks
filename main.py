
#Los requerimientos son los siguientes:
#- La API debe poder crear un usuario en la base de datos.
#- Eliminarlo.
#- devolver un listado de todos los usuarios.

#endpoints :
#"/create_user", "/delete_user", "/get_users"Los endpoints seran:

import uvicorn
import requests

from fastapi import FastAPI
from pydantic import BaseModel

# Crear la instancia de FastAPI
app = FastAPI()

class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))


# Definir el modelo de datos para un usuario (GET)
@app.get("/create_user")
def create_user(name: str):
    return {"message": f"User {name} created successfully"}


#@app.get("/delete_user")

#@app.get("/get_users")

