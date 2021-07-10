from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=32)
    power = models.BooleanField()
    action = models.TextField(default='Status')
    dev_id = models.DecimalField(max_digits=1000, decimal_places=0)


class Room(models.Model):
    name = models.CharField(max_length=24)
    location = models.CharField(max_length=32)
    image = models.TextField(default='Imagelink')
    device_count = models.DecimalField(max_digits=1000, decimal_places=0)
    power_count = models.DecimalField(max_digits=1000, decimal_places=0)