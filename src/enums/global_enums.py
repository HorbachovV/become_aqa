from enum import Enum

class GloballErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected"
    WRONG_METHOD = "Received method is not equal to expected"