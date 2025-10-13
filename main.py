
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


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))

# Crear la instancia de FastAPI
app = FastAPI()

# Definir el modelo de datos para un usuario
#@app.get("/create_user")

#@app.get("/delete_user")

#@app.get("/get_users")

