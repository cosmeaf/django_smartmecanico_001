from .models import Service
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()

    class Meta:
        model = Service
        extra_kwargs = {'user': {'required': True}}
        exclude = ['user']


class ServiceDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Service
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
