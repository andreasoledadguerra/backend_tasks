import requests

BASE_URL = "http://localhost:PORT"

#
#    
#def create_user(payload: UserCreate, db: Session = Depends(get_session)) -> UserRead:
#    new_user = User(name=payload.name)
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user)
#
#    url = f"{BASE_URL}/create_user"
#    payload = {"name": name}
#
#    # Hacer la petición POST
#     
#    response = requests.post(url, json=payload)
#    return response.json()
#
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
