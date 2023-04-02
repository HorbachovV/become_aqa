# to run test pytest .
import requests
from src.config.config import config
from src.validation.checker import Check
from src.pydantic_schemas.schemas import BasePost, Get, Post

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

def test_api_single_user():
    r = requests.get(f'{base_api_url}api/users/1')  
    response = Check(r)
    response.assert_status_code(200).validate(Get)

def test_create_user():
    data = {
        "name": "Darth Vader",
        "job": "Sith Lord",
    }
    r = requests.post(f'{base_api_url}api/users', json=data)  
    response = Check(r)
    response.assert_status_code(201).validate(Post).assert_request_method("POST")
    response_data = r.json()
    assert response_data["name"] == "Darth Vader"
    assert response_data["job"] == "Sith Lord"