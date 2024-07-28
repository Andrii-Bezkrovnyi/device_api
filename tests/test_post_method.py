import pytest
import requests

API_URL = "http://localhost:8000/devices/"


def test_create_device():
    device_data = {
        "name": "Test Device",
        "type": "Test Type",
        "login": "test_login",
        "password": "test_password",
        "location_id": 1,
        "api_user_id": 1
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(API_URL, headers=headers, json=device_data)

    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    response_data = response.json()

    assert 'id' in response_data, "Response data does not contain 'id'"
    assert response_data["name"] == device_data[
        "name"], f"Expected name: {device_data['name']}, got: {response_data['name']}"
    assert response_data["type"] == device_data[
        "type"], f"Expected type: {device_data['type']}, got: {response_data['type']}"
    assert response_data["login"] == device_data[
        "login"], f"Expected login: {device_data['login']}, got: {response_data['login']}"
    assert response_data["password"] == device_data[
        "password"], f"Expected password: {device_data['password']}, got: {response_data['password']}"
    assert response_data["location_id"] == device_data[
        "location_id"], f"Expected location_id: {device_data['location_id']}, got: {response_data['location_id']}"
    assert response_data["api_user_id"] == device_data[
        "api_user_id"], f"Expected api_user_id: {device_data['api_user_id']}, got: {response_data['api_user_id']}"


if __name__ == "__main__":
    pytest.main()
