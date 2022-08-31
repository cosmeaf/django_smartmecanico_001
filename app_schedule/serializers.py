from .models import Schedule
from rest_framework import serializers


class ScheduleSerializer(serializers.ModelSerializer):
    # Metodo para representar relacionamento
    user = serializers.StringRelatedField()
    address = serializers.StringRelatedField()
    vehicle = serializers.StringRelatedField()
    service = serializers.StringRelatedField()
    hour = serializers.StringRelatedField()
    day = serializers.StringRelatedField()

    class Meta:
        model = Schedule
        fields = '__all__'
        # depth = 2
