from django.contrib import admin
from .models import Sensor,Measurement
@admin.register(Sensor)
class adminsensor(admin.ModelAdmin):
    list_display = ['id','name',"description"]

@admin.register(Measurement)
class adminmeasurement(admin.ModelAdmin):
    list_display = ['sensor','date_time','temperature']

