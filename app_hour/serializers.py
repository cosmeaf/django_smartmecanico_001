from .models import HourAvailable
from rest_framework import serializers


class hourAvailableSerializer(serializers.ModelSerializer):
    # Metodo para representar relacionamento
    user = serializers.StringRelatedField()

    class Meta:
        model = HourAvailable
        fields = '__all__'
        #depth = 1
