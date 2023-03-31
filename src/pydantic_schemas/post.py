from pydantic import BaseModel, validator

class Post(BaseModel):
    id: int
    title: str

    @validator("id")
    def check_id_type(cls, value):
        if not type(value) == int:
            raise ValueError('Id is not integer')
        else:
            return value
        
    @validator("title")
    def check_title_type(cls, value):
        if not type(value) == str:
            raise ValueError('Title is not string')
        else:
            return value