from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone
import datetime


class PressureSensor(models.Model):
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    ID = models.AutoField(primary_key=True)
    Label = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.Label}'  
    InstallationDate = models.DateTimeField(auto_now_add=True)
    Latitude = models.DecimalField(max_digits=9, decimal_places=6)
    Longitude = models.DecimalField(max_digits=9, decimal_places=6)


class PressureReading(models.Model):
    ID = models.AutoField(primary_key=True)
    DateTime = models.DateTimeField(auto_now_add=True)
    Value = models.DecimalField(decimal_places=1, max_digits=3)
    SensorId =  models.ForeignKey(PressureSensor,on_delete=models.CASCADE)
