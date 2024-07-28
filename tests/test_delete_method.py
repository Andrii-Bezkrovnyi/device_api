import requests
import pytest

API_URL = "http://localhost:8000/devices/"

def test_delete_device():
    # Create a device to delete
    create_device_data = {
        "name": "Delete Test Device",
        "type": "Delete Test Type",
        "login": "delete_test_login",
        "password": "delete_test_password",
        "location_id": 1,
        "api_user_id": 1
    }
    headers = {'Content-Type': 'application/json'}

    response_post = requests.post(API_URL, headers=headers, json=create_device_data)
    assert response_post.status_code == 200, f"Expected status code 200 but got {response_post.status_code}"
    device_id = response_post.json()['id']

    # Delete the device
    response_delete = requests.delete(f"{API_URL}{device_id}/", headers=headers)
    assert response_delete.status_code == 200, f"Expected status code 200 but got {response_delete.status_code}"
    response_data = response_delete.json()
    assert 'message' in response_data, "Expected 'message' in response data"

    # Verify the device was deleted
    response_get = requests.get(f"{API_URL}{device_id}/", headers=headers)
    assert response_get.status_code == 404, f"Expected status code 404 but got {response_get.status_code}"
    response_get_data = response_get.json()
    assert 'error' in response_get_data, "Expected 'error' in response data"

if __name__ == "__main__":
    pytest.main()
