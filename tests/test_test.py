# to run test pytest .
import pip._vendor.requests as requests
def test_test():
    assert 1 == 1

def test_api_response_code():
    response = requests.get('https://github.com/HorbachovV/become_aqa')
    assert response.status_code == 200