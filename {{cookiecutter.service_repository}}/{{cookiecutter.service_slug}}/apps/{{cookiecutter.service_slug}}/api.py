# coding: utf-8

from rest_framework.viewsets import ModelViewSet

from .models import {{ cookiecutter.service_slug|capitalize }}
from .serializers import {{ cookiecutter.service_slug|capitalize }}Serializer


class {{ cookiecutter.service_slug|capitalize }}ViewSet(ModelViewSet):
    queryset = {{ cookiecutter.service_slug|capitalize }}.objects.all()
    serializer_class = {{ cookiecutter.service_slug|capitalize }}Serializer
    lookup_field = 'name'
