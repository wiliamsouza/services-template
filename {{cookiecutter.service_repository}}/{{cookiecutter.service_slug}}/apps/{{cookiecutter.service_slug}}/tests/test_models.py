# coding: utf-8

import pytest

from .factories import {{ cookiecutter.service_slug|capitalize }}Factory

pytestmark = pytest.mark.django_db


def test_basic_{{ cookiecutter.service_slug }}():
    {{ cookiecutter.service_slug }} = {{ cookiecutter.service_slug|capitalize }}Factory(name='{{ cookiecutter.service_slug|capitalize }} Name')

    assert '{{ cookiecutter.service_slug|capitalize }} Name' == {{ cookiecutter.service_slug }}.name
