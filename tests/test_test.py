# to run test pytest .
import requests
from src.config.config import config
# from src.enums.global_enums import GloballErrorMessages
# from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post
# from jsonschema import validate

url = config.get('BASE_URL')

def test_get_request():
    r = requests.get(url)
    response = Response(r)
   
    response.assert_status_code(200).validate(Post)
   