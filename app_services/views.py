from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer, ServiceDetailSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class ServiceModelViewSet(viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
