# tests/test_users.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# importa app y los objetos de db para poder sobreescribir
from main import app
from db import Base, get_session
from models import User

# 1) Crear engine en memoria para tests (aislado)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2) Fixture para inicializar la BD en memoria y devolver sesión
@pytest.fixture(scope="function")
def db_session():
    # crea tablas nuevas
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)  # limpia entre tests

# 3) Override de dependencia get_db para usar la sesión de prueba
@pytest.fixture(scope="function")
def client(db_session):
    def _get_test_db():
        try:
            yield db_session
        finally:
            pass
    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

# --- Tests individuales por endpoint ---

def test_create_user(client):
    resp = client.post("/create_user", json={"name": "Andy"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] is not None
    assert data["name"] == "Andy"

def test_get_users_empty(client):
    resp = client.get("/get_users")
    assert resp.status_code == 200
    assert resp.json() == []

def test_get_users_with_one(client):
    # crea directamente usando endpoint
    client.post("/create_user", json={"name":"User1"})
    resp = client.get("/get_users")
    assert resp.status_code == 200
    assert len(resp.json()) == 1
    assert resp.json()[0]["name"] == "User1"

def test_delete_user(client):
    # crear y borrar
    r = client.post("/create_user", json={"name":"ToDelete"})
    uid = r.json()["id"]
    del_resp = client.delete(f"/delete_user/{uid}")
    assert del_resp.status_code == 204
    # comprobar ya no existe
    get_resp = client.get("/get_users")
    assert all(u["id"] != uid for u in get_resp.json())

def test_delete_user_not_found(client):
    resp = client.delete("/delete_user/9999")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "User not found"
