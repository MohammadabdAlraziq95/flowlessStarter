

from Pressure.models import PressureReading, PressureSensor
from rest_framework import  serializers


class PressureSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PressureSensor
        fields = ['ID', 'Label', 'InstallationDate', 'Latitude' , 'Longitude']


class PressureReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PressureReading
        fields = ['ID', 'DateTime', 'Value', 'SensorId']
