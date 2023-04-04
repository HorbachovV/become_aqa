import requests
from applications.api.github_api import GitHubApiClient



# def test_existing_repo_can_be_found():
#     # r = requests.get(f'{github_api_url}')
#     # assert r.status_code == 200
#     pass

def test_non_existing_repo_can_not_be_found():
    client = GitHubApiClient()
    r = client.search_repo("become_aqa")
    assert r.status_code == 200
    assert r.json()['total_count'] > 0

    
# def test_search_not_working_without_q():
#     pass


# def test_search_repo():
#         github_api_url = "https://api.github.com/"
#         repo_name = "become_aqa"
#         r = requests.get(f"{github_api_url}search/repositories", params={'q': repo_name})
        
#         print(r)
#         print(r.json())

