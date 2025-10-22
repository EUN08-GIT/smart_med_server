from django.urls import path
from .views import receive_sensor_data

urlpatterns = [ path('data/', receive_sensor_data) ]