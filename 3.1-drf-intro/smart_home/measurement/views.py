# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor,Measurement

from rest_framework.views import APIView
from rest_framework.generics import  ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .serializers import SerializerSensor,SerializerMeasurement
class SensorView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SerializerSensor
    def post(self,request):
        sensor_data=request.data
        Sensor.objects.create(name=sensor_data.get('name'),description=sensor_data.get('description'))
        return Response(data=sensor_data)


class MeasurementView(viewsets.ModelViewSet):
    queryset= Measurement.objects.all()
    serializer_class = SerializerMeasurement

class update_sensor_view(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SerializerSensor

    def patch (self,request,pk):
        data=request.data
        name = data.get('name')
        description = data.get('description')
        sensor_update=Sensor.objects.filter(id=pk).all()
        if description:
            sensor_update.update(description=description).save()
        if name:
            sensor_update.update(name=name).save()
        return Response(data=data)

class measurementView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = SerializerMeasurement

    def post(self, request):
        data = request.data
        Measurement.objects.create(sensor=data.get('sensor'), temperature=data.get('temperature'))
        return Response(data=data)

