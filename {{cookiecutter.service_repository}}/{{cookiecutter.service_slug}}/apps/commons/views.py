# coding: utf-8

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response


class Health(generics.RetrieveAPIView):
    """
    Service's health check
    """
    csrf_exempt = True
    permission_classes = (permissions.AllowAny,)

    def retrieve(request, *args, **kwargs):
        data = {
            "status": "OK",
        }
        return Response(data)

health_check = Health.as_view()
