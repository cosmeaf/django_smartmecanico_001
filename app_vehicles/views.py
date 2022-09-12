from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleDetailSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class VehicleModelViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return VehicleSerializer
        else:
            return VehicleDetailSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all().filter(is_active=True)
        else:
            return self.queryset.filter(user=user, is_active=True)
