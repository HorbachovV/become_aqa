# from jsonschema import validate
from src.enums.global_enums import GloballErrorMessages

class Response:
    def __init__(self, response):
        self.responce = response
        self.response_json = response.json()
        self.responce_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            # schema.parse_obj(self.response_json)
            for item in self.response_json:
                schema.parse_obj(item)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.responce_status in status_code, GloballErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.responce_status == status_code, GloballErrorMessages.WRONG_STATUS_CODE.value
        return self
    
    # def validate_dict(self, schema):
    #     for item in self.response_json:
    #         schema.parse_obj(item)
        