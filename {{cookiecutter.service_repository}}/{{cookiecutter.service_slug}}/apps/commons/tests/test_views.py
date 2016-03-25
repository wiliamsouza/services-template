# coding: utf-8
import json


def test_health_return_200(client):
    response = client.get('/health')
    assert response.status_code == 200


def test_health_using_POST_should_return_405(client):
    response = client.post('/health')
    assert response.status_code == 405


def test_health_using_PUT_should_return_405(client):
    response = client.put('/health')
    assert response.status_code == 405


def test_health_using_PATCH_should_return_405(client):
    response = client.patch('/health')
    assert response.status_code == 405


def test_health_return_status(client):
    response = client.get('/health')
    response_json = json.loads(response.content.decode('utf-8'))
    assert response_json['status'] == 'OK'
