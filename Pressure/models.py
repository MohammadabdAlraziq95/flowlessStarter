from re import T
from django.db import models
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
import datetime
from django.utils.crypto import get_random_string

class PressureSensor(models.Model):
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    ID = models.AutoField(primary_key=True)

    def validate_label(value):
        if value.startswith('PSSR'):
            return value
        else:
            raise ValidationError("This Field must start with PSSR")
    Label = models.CharField(max_length=100,validators=[validate_label])

    def __str__(self):
        return f'{self.Label}'  
    InstallationDate = models.DateTimeField(auto_now_add=True)
    Latitude = models.DecimalField(max_digits=9, decimal_places=6)
    Longitude = models.DecimalField(max_digits=9, decimal_places=6)
    def compute_default():
       return get_random_string(length=10)
    serial_number= models.CharField(max_length=100, default=compute_default,null=True,editable=False)


class PressureReading(models.Model):
    ID = models.AutoField(primary_key=True)
    DateTime = models.DateTimeField(auto_now_add=True)
    Value = models.DecimalField(decimal_places=1, max_digits=3)
    # SensorId =  models.ForeignKey(PressureSensor,on_delete=models.CASCADE)
    SensorId = models.ManyToManyField(PressureSensor)
    