import requests

if __name__ == "__main__":
    response = requests.get("http://localhost:8000/")
    print(response.status_code)
    print(response.json())