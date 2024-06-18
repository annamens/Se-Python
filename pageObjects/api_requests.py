import string
import requests
import json
import random
import pytest
from jsonschema import validate , validators
#serialization
data = {'name': 'John', 'age': 30, 'city': 'New York'}
serialized_data = json.dumps(data)
#Deserialization
deserialized_data= json.loads(serialized_data)
def random_string(n):
    result=''.join(random.choices(string.ascii_lowercase,k=n))
    return result

base_url = "https://gorest.co.in"
auth_token = "Bearer ec645b7dcc86b4e08738d3af382e68fe65e7b345510b95b2cb86ed806b79e1be"
headers = {"Authorization": auth_token}

#GET request
def get_request(user_id):
    url = base_url+"/public/v2/users/%s"%(user_id)

    response=requests.get(url,headers=headers)
    json_response=response.json()
    pretty_json = json.dumps(json_response, indent=4)
    assert response.status_code == 200
    print("GET response:",pretty_json)
    print("GET request was done...")

#POST request
def post_request():
    url=base_url+"/public/v2/users"
    data= {
        "name": "srinii",
        "email": random_string(6)+"@email.com",
        "gender": "male",
        "status": "active"
    }
    response=requests.post(url, json=data,headers=headers)
    assert response.status_code == 201
    json_data= response.json()
    pretty_json=json.dumps(response.json(), indent=4)
    print("POST response",pretty_json)
    user_id = json_data["id"]
    assert json_data["name"] == "srinii"
    return user_id
    print("POST request was done...")
#put/patch put=update existing data/create new data patch = update partial data
#PUT request
def put_request(user_id):
    url=base_url+f"/public/v2/users/{user_id}"
    data = {
        "name": "Ramesh",
        "email": random_string(6) + "@email.com",
        "gender": "male",
        "status": "Inactive"
    }
    response=requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data= response.json()
    assert json_data["id"]== user_id
    assert json_data["name"] == "Ramesh"
    pretty_json = json.dumps(json_data,indent=4)
    print("PUT response",pretty_json)
    print("PUT request was done...")
#DELETE request
def delete_request(user_id):
    url = base_url+f"/public/v2/users/{user_id}"
    response = requests.delete(url,headers=headers)
    assert response.status_code == 204
    print("DELETE request was done...")

get_request("6875559")
user_id =post_request()
put_request(user_id)
delete_request(user_id)

test_data = [
    {"url": base_url+"/public/v2/users/6875562", "expected_status_code": 200},
    {"url":  base_url+"/public/v2/users/6875558", "expected_status_code": 200},
    {"url":  base_url+"/public/v2/users/6875559", "expected_status_code": 404},
    # Add more test cases as needed
]

@pytest.mark.parametrize("test_input", test_data)
def test_api_request(test_input):
    response = requests.get(test_input["url"], headers=headers)
    assert response.status_code == test_input["expected_status_code"]