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
from os import uname
from pyexpat import model
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from Pressure.views import Home, PressureReadingViewSet, PressureSensorViewSet, calculate_class_based, func_pressure_readings
from rest_framework import routers
from django.urls import include, re_path

router = routers.DefaultRouter()
router.register(r'ps', PressureSensorViewSet)
router.register(r'pr', PressureReadingViewSet)
from Pressure import views
urlpatterns = [
    path('api/home/', views.Home , name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('polls/', include('polls.urls')),
    re_path(r'func_pressure_readings/', func_pressure_readings, name='func_pressure_readings'),
    path('calculate_class_based', views.calculate_class_based.as_view(), name='calculate_class_based'),
]
