from .models import Schedule
from rest_framework import serializers


class ScheduleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Schedule
        fields = '__all__'
        depth = 1
        extra_kwargs = {'user': {'required': True}}


class ScheduleDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Schedule
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
