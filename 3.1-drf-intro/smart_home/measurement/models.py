from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=60)

class Measurement(models.Model):
    sensor=models.ForeignKey(Sensor,on_delete=models.CASCADE,related_name='measurements')
    date_time=models.DateTimeField(auto_now_add=True)
    temperature=models.FloatField()

