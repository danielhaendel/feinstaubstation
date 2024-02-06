from django.db import models

# Create your models here.

class SDS011_3659_2022(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_id = models.IntegerField(default=3659)
    sensor_type = models.CharField(max_length=6,default='SDS011')
    location = models.IntegerField(null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    timestamp = models.DateTimeField()
    p1 = models.FloatField(null=True)
    durp1 = models.FloatField(null=True)
    ratiop1 = models.FloatField(null=True)
    p2 = models.FloatField(null=True)
    durp2 = models.FloatField(null=True)
    ratiop2 = models.FloatField(null=True)

    def __str__(self):
        return f"{self.id} - {self.sensor_type}"


class DHT22_3660_2022(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_id = models.IntegerField(default=3660)
    sensor_type = models.CharField(max_length=6,default='DHT22')
    location = models.IntegerField(null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    timestamp = models.DateTimeField(null=True)
    temperature = models.FloatField(null=True)
    humidity = models.FloatField(null=True)

    def __str__(self):
        return f"{self.id} - {self.sensor_type}"
    