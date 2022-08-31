from .models import HourAvailable
from rest_framework import viewsets
from .serializers import hourAvailableSerializer
# ViewSets define the view behavior.


class hourAvailableViewSet(viewsets.ModelViewSet):
    """
    ViewSets Version 1
    """
    queryset = HourAvailable.objects.all()
    serializer_class = hourAvailableSerializer
