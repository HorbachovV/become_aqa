from src.enums.global_enums import GloballErrorMessages

class Check:
    def __init__(self, response):
        self.responce = response
        self.response_json = response.json()
        self.responce_status = response.status_code
        self.responce_method = response.request.method

    # def validate(self, schema):
    #     if isinstance(self.response_json, list):
    #         for item in self.response_json:
    #             schema.parse_obj(item)
    #     elif isinstance(self.response_json, dict):
    #         for item in self.response_json['data']:
    #             schema.parse_obj(item)
    #     elif isinstance(self.response_json, dict):
    #         schema.parse_obj(self.response_json['data'])
    #     else:
    #         for item in self.response_json:
    #             schema.parse_obj(item)
    #     return self
    
    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        elif isinstance(self.response_json, dict):
            if 'data' in self.response_json:
                data = self.response_json['data']
                if isinstance(data, list):
                    for item in data:
                        schema.parse_obj(item)
                else:
                    schema.parse_obj(data)
            else:
                schema.parse_obj(self.response_json)
        else:
            for item in self.response_json:
                schema.parse_obj(item)
        return self


    def assert_request_method(self, status_method):
        assert self.responce_method == status_method, GloballErrorMessages.WRONG_METHOD.value

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.responce_status in status_code, GloballErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.responce_status == status_code, GloballErrorMessages.WRONG_STATUS_CODE.value
        return self
        