# to run test pytest .
import requests
from src.config.config import config
from src.validation.checker import Check
from src.pydantic_schemas.schemas import BasePost, Get

base_url = config.get("BASE_URL")
base_api_url = config.get("BASE_API_URL")

def test_basic():
    r = requests.get(base_url)
    response = Check(r)
    response.assert_status_code(200).validate(BasePost).assert_request_method("GET")

def test_api_response_code():
    r = requests.get(f'{base_api_url}api/users')    
    response = Check(r)
    response.assert_status_code(200).validate(Get)
    for item in r.json()['data']:
        print(item)

def test_api_single_user():
    r = requests.get(f'{base_api_url}api/users/1')  
    response = Check(r)
    response.assert_status_code(200).validate(Get)
    for item in r.json():
        print(item)
    print(r.json()['data'])