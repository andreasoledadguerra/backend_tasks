import requests

if __name__ == "__main__":
    response = requests.post("http://localhost:8000/create_user")
    print(response.status_code)
    print(response.json())
