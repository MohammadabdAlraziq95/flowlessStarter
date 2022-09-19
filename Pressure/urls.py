from django.urls import path

from Pressure.models import PressureReading, PressureSensor

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]