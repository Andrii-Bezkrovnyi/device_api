import requests
import pytest

API_URL = "http://localhost:8000/devices/"

def test_put_device():
    # Create a device to update
    create_device_data = {
        "name": "Old Test Device",
        "type": "Old Test Type",
        "login": "old_test_login",
        "password": "old_test_password",
        "location_id": 1,
        "api_user_id": 1
    }
    headers = {'Content-Type': 'application/json'}

    response_post = requests.post(API_URL, headers=headers, json=create_device_data)
    assert response_post.status_code == 200, f"Expected status code 200 but got {response_post.status_code}"
    device_id = response_post.json()['id']

    # Update the device
    update_device_data = {
        "name": "Updated Test Device",
        "type": "Updated Test Type",
        "login": "updated_test_login",
        "password": "updated_test_password",
        "location_id": 1,
        "api_user_id": 1
    }

    response_put = requests.put(f"{API_URL}{device_id}/", headers=headers, json=update_device_data)
    assert response_put.status_code == 200, f"Expected status code 200 but got {response_put.status_code}"
    response_data = response_put.json()

    assert response_data['name'] == update_device_data['name'], f"Expected name to be {update_device_data['name']} but got {response_data['name']}"
    assert response_data['type'] == update_device_data['type'], f"Expected type to be {update_device_data['type']} but got {response_data['type']}"
    assert response_data['login'] == update_device_data['login'], f"Expected login to be {update_device_data['login']} but got {response_data['login']}"
    assert response_data['password'] == update_device_data['password'], f"Expected password to be {update_device_data['password']} but got {response_data['password']}"
    assert response_data['location_id'] == update_device_data['location_id'], f"Expected location_id to be {update_device_data['location_id']} but got {response_data['location_id']}"
    assert response_data['api_user_id'] == update_device_data['api_user_id'], f"Expected api_user_id to be {update_device_data['api_user_id']} but got {response_data['api_user_id']}"

if __name__ == "__main__":
    pytest.main()
