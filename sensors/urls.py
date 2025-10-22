from django.urls import path
from .views import receive_sensor_data

urlpatterns = [
    path('sensor/', receive_sensor_data),
]