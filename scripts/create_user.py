
#from fastapi import Depends
#from sqlalchemy.orm import Session
#
#@app.post("/create_user", response_model=UserRead, status_code=201)
#def create_user(payload: UserCreate, db: Session = Depends(get_session)) -> UserRead:
#    # Crear la instancia ORM con los datos validados por Pydantic
#    new_user = User(name=payload.name)
#
#    # Persistir en la DB
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user)
#
#    # Devolver el objeto ORM; FastAPI lo serializa usando response_model (orm_mode=True)
#    return new_user
#

    
#def create_user(payload: UserCreate, db: Session = Depends(get_session)) -> UserRead:
#    new_user = User(name=payload.name)
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user)
#
#    # Hacer la petición POST
#    response = requests.post(url, json=payload)

#    return UserRead(
#        data= response.json(),
#        status_code=response.status_code,
#        success=response.status_code == 200)

