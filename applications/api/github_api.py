import requests
from src.config.config import config

github_api_url = config.get("GITHUB_BASE_API")

class GitHubApiClient:

    def search_repo(self, repo_name):
        r = requests.get(f"{github_api_url}search/repositories", params={'q': repo_name})
        
        return r
    
    def login(username, password):
        print(f"Do login with {username}:{password}")
        token = requests.post("https://api.github.com/login")

    def logout(username, password):
        print("Do loguot")
        