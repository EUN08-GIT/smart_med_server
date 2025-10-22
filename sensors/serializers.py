from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['sensor_value', 'is_opened', 'heart_rate']
