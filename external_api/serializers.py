from .models import AirQuality, Device
from rest_framework import serializers


class AirQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirQuality
        fields = ('pm25', 'pm100', 'pm10', 'created_at', 'device_id')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_id', 'name', 'location', 'latitude', 'longitude')


class AverageAirQualitySerializer(serializers.Serializer):
    created_at_trunced_hour = serializers.DateTimeField()
    avg_pm100 = serializers.IntegerField()
    avg_pm25 = serializers.IntegerField()
    avg_pm10 = serializers.IntegerField()
