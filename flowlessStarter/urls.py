"""flowlessStarter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pyexpat import model
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.contrib.auth.models import User
from Pressure.models import PressureReading, PressureSensor
from rest_framework import routers, serializers, viewsets
from django_filters.rest_framework import DjangoFilterBackend


class PressureSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PressureSensor
        fields = ['ID', 'Label', 'InstallationDate', 'Latitude' , 'Longitude']


class PressureReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PressureReading
        fields = ['ID', 'DateTime', 'Value', 'SensorId']

class PressureSensorViewSet(viewsets.ModelViewSet):

     queryset = PressureSensor.objects.all()
     serializer_class = PressureSensorSerializer
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['ID', 'InstallationDate']

class PressureReadingViewSet(viewsets.ModelViewSet):

     queryset = PressureReading.objects.all()
     serializer_class = PressureReadingSerializer
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['ID', 'DateTime']
# router 
router = routers.DefaultRouter()
router.register(r'ps', PressureSensorViewSet)
router.register(r'pr', PressureReadingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Pressure/', include('Pressure.urls')),
    path('api/', include(router.urls)),
    path('rest/', include('rest_framework.urls', namespace='rest_framework'))


]
