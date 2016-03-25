# coding: utf-8

import uuid

from django.db import models

from model_utils.models import TimeStampedModel


class {{ cookiecutter.service_slug|capitalize }}(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
