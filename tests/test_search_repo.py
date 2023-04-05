import requests
from src.applications.api.github_api import GitHubApiClient
from src.generators.fake_data import FakeData



def test_existing_repo_can_be_found():
    client = GitHubApiClient()
    r = client.search_repo("become_aqa")
    assert r.status_code == 200
    assert r.json()['total_count'] > 0

def test_non_existing_repo_can_not_be_found():
    client = GitHubApiClient()
    fake = FakeData()
    repo_name = fake.random_repo_name()
    r = client.search_repo(repo_name)
    assert r.status_code == 200
    assert r.json()['total_count'] == 0

    
def test_search_not_working_without_q():
    pass