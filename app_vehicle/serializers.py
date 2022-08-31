from .models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Vehicle
        fields = '__all__'
        #depth = 1
