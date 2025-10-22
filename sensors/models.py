from django.db import models

# Create your models here.
# sensors/models.py
from django.db import models
from users.models import User  # 연관 필요시

class SensorData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_opened = models.BooleanField(default=False)
    sensor_value = models.IntegerField()
    heart_rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


