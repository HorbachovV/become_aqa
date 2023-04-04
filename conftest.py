import pytest
from applications.api.github_api import GitHubApiClient

class User:
    def __init__(self, age) -> None:
        # datadabase interaction
        self.age = age

    def remove(self):
        # database interaction
        self.age = None


@pytest.fixture(scope="session")
def user():
    # before test
    print("Create user")
    user = User(42)

    # pass user object to test
    yield user

    # after test
    print("Remove user")
    user.remove()

# @pytest.fixture
# def github_api_client():
#     api_client = GitHubApiClient()
#     api_client.login("username", "userpassword")

#     yield github_api_client

#     github_api_client.logout()