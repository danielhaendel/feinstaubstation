from django.db import models

# Create your models here.

class SDS011_3659_2022(models.Model):
    id = models.AutoField(primary_key=True)
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"timestamp: {self.timestamp}"


class DHT22_3660_2022(models.Model):
    id = models.AutoField(primary_key=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"timestamp: {self.timestamp}"
    