from .models import Service
from rest_framework import viewsets
from .serializers import ServiceSerializer
# ViewSets define the view behavior.


class ServiceViewSet(viewsets.ModelViewSet):
    """
    ViewSets Version 1
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
