import requests
from constants import url
from utils.status_code import status_ok

def main() -> None:
    response = requests.get(url)
    if status_ok(response.status_code):
        print(response.json()['text'])

if __name__ == "__main__":
    main()