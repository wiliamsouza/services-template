# coding: utf-8


import pytest

from rest_framework.authtoken.models import Token


@pytest.fixture()
def user_api(db, django_user_model, django_username_field):
    """A Django API user """
    UserModel = django_user_model
    username_field = django_username_field

    try:
        user = UserModel.objects.get(**{username_field: 'test'})
    except UserModel.DoesNotExist:
        extra_fields = {}
        if username_field != 'username':
            extra_fields[username_field] = 'test'
        user = UserModel.objects.create_user(
            'test', '{{ cookiecutter.email }}', 'password', **extra_fields)

    return user


@pytest.fixture()
def client_api(db, user_api):
    """A Django API client logged in"""
    from django.test.client import Client

    token, _ = Token.objects.get_or_create(user=user_api)
    client = Client(HTTP_AUTHORIZATION='Token {}'.format(token))
    return client
