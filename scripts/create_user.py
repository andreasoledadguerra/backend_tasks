import requests

BASE_URL = "http://localhost:PORT"
url = f"{BASE_URL}/create_user"
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

#--------------------EJEMPLO------------------------------------------
## Decorador para definir un endpoint GET
#@app.get("/temperature")
#def get_temperature_by_dates(lat: float, lon: float, date_i: str, date_f: str) -> WeatherResponse:
#    params = {
#        "latitude": lat,
#        "longitude": lon,
#        "hourly": "temperature_2m",
#        "start_date": date_i,
#        "end_date": date_f,
#        "timezone": "UTC"
#    }
#
#    # Hace una petición a Open-Meteo
#    response = requests.get(url_forecast, params=params)
#    
#    return WeatherResponse(
#        data=response.json(),           # Extrae los datos JSON
#        status_code=response.status_code,  # Copia el status code
#        success=response.status_code == 200  # Marca si fue exitosa
#    )
