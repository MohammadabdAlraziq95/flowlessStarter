

# from django.db import models


# class PressureSensor(models.Model):
#     ID = models.AutoField(primary_key=True)
#     Label = models.CharField(max_length=100)
#     InstallationDate = models.DateTimeField()
#     Latitude = models.DecimalField(max_digits=9, decimal_places=6)
#     Longitude = models.DecimalField(max_digits=9, decimal_places=6)


# class PressureReading(models.Model):
#     ID = models.AutoField(primary_key=True)
#     DateTime = models.DateTimeField()
#     Value = models.DecimalField(decimal_places=3, max_digits=3)
#     SensorId =  models.IntegerField()
