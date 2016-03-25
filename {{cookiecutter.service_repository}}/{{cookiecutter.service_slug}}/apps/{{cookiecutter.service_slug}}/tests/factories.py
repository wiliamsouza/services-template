# coding: utf-8

import factory


from ..models import {{ cookiecutter.service_slug|capitalize }}


class {{ cookiecutter.service_slug|capitalize }}Factory(factory.DjangoModelFactory):

    class Meta:
        model = {{ cookiecutter.service_slug|capitalize }}

    name = factory.Sequence(lambda n: '{{ cookiecutter.service_slug|capitalize }} {0}'.format(n))
