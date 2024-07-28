import pytest
import requests

# URL вашего API
BASE_URL = "http://localhost:8000/"

def test_get_all_devices():
    response = requests.get(f"{BASE_URL}/devices/")
    assert response.status_code == 200

    # Проверяем, что ответ - это список
    devices = response.json()
    assert isinstance(devices, list)

def test_get_device_by_id():
    # Замените 1 на ID устройства, которое вы знаете, что оно существует в базе данных
    device_id = 1
    response = requests.get(f"{BASE_URL}/devices/{device_id}/")
    assert response.status_code == 200

    # Проверяем, что ответ - это объект устройства
    device = response.json()
    assert isinstance(device, dict)
    assert device['id'] == device_id

def test_get_device_by_invalid_id():
    # Замените 99999 на ID, который вы знаете, что не существует в базе данных
    invalid_device_id = 99999
    response = requests.get(f"{BASE_URL}/devices/{invalid_device_id}/")
    assert response.status_code == 404

    # Проверяем, что ответ содержит сообщение об ошибке
    error_response = response.json()
    assert 'error' in error_response
    assert error_response['error'] == 'Device not found!'

if __name__ == "__main__":
    pytest.main()
