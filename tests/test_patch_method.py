import requests
import pytest

API_URL = "http://localhost:8000/devices/"

def test_patch_device():
    # Create a device to update
    create_device_data = {
        "name": "Patch Test Device",
        "type": "Patch Test Type",
        "login": "patch_test_login",
        "password": "patch_test_password",
        "location_id": 1,
        "api_user_id": 1
    }
    headers = {'Content-Type': 'application/json'}

    response_post = requests.post(API_URL, headers=headers, json=create_device_data)
    assert response_post.status_code == 200, f"Expected status code 200 but got {response_post.status_code}"
    device_id = response_post.json()['id']

    # Patch the device
    patch_data = {
        "name": "Updated Patch Test Device"
    }
    response_patch = requests.patch(f"{API_URL}{device_id}/", headers=headers, json=patch_data)
    assert response_patch.status_code == 200, f"Expected status code 200 but got {response_patch.status_code}"
    response_data = response_patch.json()
    assert response_data['name'] == patch_data['name'], f"Expected device name to be updated to {patch_data['name']}"

    # Verify the device was updated
    response_get = requests.get(f"{API_URL}{device_id}/", headers=headers)
    assert response_get.status_code == 200, f"Expected status code 200 but got {response_get.status_code}"
    response_get_data = response_get.json()
    assert response_get_data['name'] == patch_data['name'], f"Expected device name to be {patch_data['name']}"

    # Cleanup: Delete the device
    response_delete = requests.delete(f"{API_URL}{device_id}/", headers=headers)
    assert response_delete.status_code == 200, f"Expected status code 200 but got {response_delete.status_code}"

if __name__ == "__main__":
    pytest.main()
