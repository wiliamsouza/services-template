# coding: utf-8

from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('apps.{{ cookiecutter.service_slug }}.routes', namespace='{{ cookiecutter.service_slug }}')),
]
