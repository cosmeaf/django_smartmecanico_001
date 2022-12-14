from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Schedule
from .serializers import ScheduleSerializer, ScheduleDetailSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class ScheduleModelViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ScheduleSerializer
        else:
            return ScheduleDetailSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all().filter(is_active=True)
        else:
            return self.queryset.filter(user=user, is_active=True)
