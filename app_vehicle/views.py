from .models import Vehicle
from rest_framework import viewsets
from .serializers import VehicleSerializer
# ViewSets define the view behavior.


class VehicleViewSet(viewsets.ModelViewSet):
    """
    ViewSets Version 1
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
