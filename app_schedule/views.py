from .models import Schedule
from rest_framework import viewsets
from .serializers import ScheduleSerializer
# ViewSets define the view behavior.


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    ViewSets Version 1
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
