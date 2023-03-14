import pytest

class User:
    def __init__(self, age=None):
        self.age = age
    
    def remove(self):
        self.age = None

@pytest.fixture(scope='session')
def user():
    print('Create user')
    user = User(42)
    yield user
    print('Remove user')
    user.remove()