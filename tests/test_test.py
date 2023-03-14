# to run test pytest .
import pip._vendor.requests as requests





def test_user_age_is_42(user):
    
    assert user.age == 42

# def test_user_age_is_50(user):
    
#     assert user.age == 50

# def test_api_response_code():
#     response = requests.get('https://github.com/HorbachovV/become_aqa')
#     assert response.status_code == 200