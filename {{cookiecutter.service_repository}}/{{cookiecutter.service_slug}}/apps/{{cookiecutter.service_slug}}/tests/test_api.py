# coding: utf-8

import json

import pytest
from rest_framework import status

from ..models import {{ cookiecutter.service_slug|capitalize }}
from .factories import {{ cookiecutter.service_slug|capitalize }}Factory

pytestmark = pytest.mark.django_db


def test_get_{{ cookiecutter.service_slug }}_all(client_api):
    url = '/v1/{{ cookiecutter.service_slug }}/'
    response = client_api.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == []

    {{ cookiecutter.service_slug|capitalize }}Factory(name='Drugstore')
    {{ cookiecutter.service_slug|capitalize }}Factory(name='Marketplace')
    {{ cookiecutter.service_slug|capitalize }}Factory(name='Amope')

    response = client_api.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3


def test_get_{{ cookiecutter.service_slug }}(client_api):
    {{ cookiecutter.service_slug }} = {{ cookiecutter.service_slug|capitalize }}Factory()

    url = '/v1/{{ cookiecutter.service_slug }}/{}/'.format({{ cookiecutter.service_slug }}.name)

    response = client_api.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == {{ cookiecutter.service_slug }}.name


def test_get_{{ cookiecutter.service_slug }}_invalid(client_api):
    url = '/v1/{{ cookiecutter.service_slug }}/invalid/'

    response = client_api.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['detail'] == 'Not found.'


def test_post_{{ cookiecutter.service_slug }}(client_api):
    url = '/v1/{{ cookiecutter.service_slug }}/'
    data = {'name': 'Drugstore'}

    response = client_api.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED
    assert {{ cookiecutter.service_slug|capitalize }}.objects.filter(name='Drugstore').exists(), 'Not created'


def test_post_{{ cookiecutter.service_slug }}_without_data(client_api):
    url = '/v1/{{ cookiecutter.service_slug }}/'
    data = {}

    response = client_api.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['name'] == ['This field is required.']


def test_put_{{ cookiecutter.service_slug }}(client_api):
    {{ cookiecutter.service_slug }} = {{ cookiecutter.service_slug|capitalize }}Factory()

    url = '/v1/{{ cookiecutter.service_slug }}/{}/'.format({{ cookiecutter.service_slug }}.name)

    data = {'name': 'Amope'}

    response = client_api.put(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Amope'


def test_patch_{{ cookiecutter.service_slug }}(client_api):
    {{ cookiecutter.service_slug }} = {{ cookiecutter.service_slug|capitalize }}Factory()

    url = '/v1/{{ cookiecutter.service_slug }}/{}/'.format({{ cookiecutter.service_slug }}.name)
    data = {'name': 'Amope'}

    response = client_api.patch(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Amope'


def test_delete_{{ cookiecutter.service_slug }}_success(client_api):
    {{ cookiecutter.service_slug }} = {{ cookiecutter.service_slug|capitalize }}Factory()

    url = '/v1/{{ cookiecutter.service_slug }}/{}/'.format({{ cookiecutter.service_slug }}.name)

    response = client_api.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert {{ cookiecutter.service_slug|capitalize }}.objects.count() == 0


def test_delete_{{ cookiecutter.service_slug }}_invalid(client_api):
    url = '/v1/{{ cookiecutter.service_slug }}/invalid/'

    response = client_api.delete(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['detail'] == 'Not found.'
