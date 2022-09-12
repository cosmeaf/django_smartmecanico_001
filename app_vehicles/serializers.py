from .models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Vehicle
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}


class VehicleDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Vehicle
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
