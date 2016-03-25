# coding: utf-8

from django.apps import AppConfig


class {{ cookiecutter.service_slug|capitalize }}Config(AppConfig):
    name = 'apps.{{ cookiecutter.service_slug }}'
