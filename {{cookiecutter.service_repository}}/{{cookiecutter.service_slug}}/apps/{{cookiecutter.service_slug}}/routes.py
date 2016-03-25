# coding: utf-8

from rest_framework_extensions.routers import ExtendedDefaultRouter

from .api import {{ cookiecutter.service_slug|capitalize }}ViewSet


router = ExtendedDefaultRouter()
(
    router.register(r"{{ cookiecutter.service_slug }}", {{ cookiecutter.service_slug|capitalize }}ViewSet,
                    base_name="{{ cookiecutter.service_slug }}"),
)

urlpatterns = router.urls
