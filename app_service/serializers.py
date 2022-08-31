from .models import Service
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    # Metodo para representar relacionamento
    user = serializers.StringRelatedField()

    class Meta:
        model = Service
        fields = '__all__'
        # depth = 1
