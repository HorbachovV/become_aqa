# to run test pytest .
from src.config.config import Config


def test_user_age_is_42(user):
    
    assert user.age == 42

def test_user_age_is_50(user):
    
    assert user.age == 50

def test_config():
    print(Config.get("BASE_URL"))