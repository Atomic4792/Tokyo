"""dotenv import load_dotenv
import requests

load_dotenv()  # loads .env into environment variables

def get_random_api_data(): #missing return type indicator
    url = os.getenv("ENDPOINT_URL")
    token = os.getenv("JSON_API_TOKEN")
    print(token)

    headers = {"Authorization": f"Bearer {token}"}

    r = requests.get(url, headers=headers)

    return  r.json()"""
from pathlib import Path
import json

data_path = Path(__file__).parent / "data.json"
def get_user_data() -> list:
  with data_path.open() as f:
      data = json.load(f)
      return data