from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(max_length=60, null=True)


