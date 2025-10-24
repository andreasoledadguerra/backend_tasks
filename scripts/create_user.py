import requests

if __name__ == "__main__":
    data = {"name": "Andy"}

    response = requests.post("http://localhost:8000/create_user", json=data)
    print(response.status_code)
    print(response.json())
