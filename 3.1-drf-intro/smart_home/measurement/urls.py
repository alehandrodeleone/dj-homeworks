from django.urls import path
from .views import SensorView,MeasurementView

urlpatterns = [
    path('sensor/', SensorView.as_view({'get': 'list'})),


    # TODO: зарегистрируйте необходимые маршруты
]
