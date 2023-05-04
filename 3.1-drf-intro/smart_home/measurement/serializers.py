from rest_framework import serializers
from .models import Measurement,Sensor

class SerializerSensor(serializers.ModelSerializer):
    class Meta:
        model=Sensor
        fields = ['id', 'name', 'description']

class SerializerMeasurement(serializers.ModelSerializer):

    class Meta:
        model=Measurement
        fields=['sensor','temperature']