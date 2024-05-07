
import pytest
import requests

base_url = "https://gorest.co.in"
auth_token = "Bearer ec645b7dcc86b4e08738d3af382e68fe65e7b345510b95b2cb86ed806b79e1be"
headers = {"Authorization": auth_token}


test_data = [
    {"url": base_url+"/public/v2/users/6875562", "expected_status_code": 200},
    {"url":  base_url+"/public/v2/users/6875558", "expected_status_code": 200},
    {"url":  base_url+"/public/v2/users/6875559", "expected_status_code": 404},
    # Add more test cases as needed
]
import allure


@pytest.mark.parametrize("test_input", test_data)
def test_api_request(test_input):
    response = requests.get(test_input["url"], headers=headers)
    assert response.status_code == test_input["expected_status_code"]


