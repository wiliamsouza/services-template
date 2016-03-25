# coding: utf-8

from rest_framework import serializers

from .models import {{ cookiecutter.service_slug|capitalize }}


class {{ cookiecutter.service_slug|capitalize }}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {{ cookiecutter.service_slug|capitalize }}
        fields = ('name', )
