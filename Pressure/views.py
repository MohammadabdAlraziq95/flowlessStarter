import datetime
# from http.client import HTTPResponse
from django.http import HttpResponse
import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import  viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response 
from rest_framework import viewsets, views
from rest_framework import response
from django.views import View
from Pressure.models import PressureReading, PressureSensor
from Pressure.serializer import PressureReadingSerializer, PressureSensorSerializer
# Create your views here.


from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from django.core import serializers


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


class calculate_class_based(views.APIView):

    def get(self, request):
        start = datetime.datetime.fromisoformat(request.GET.get('since'))
        end = datetime.datetime.fromisoformat(request.GET.get('until'))
        queryset = PressureReading.objects.filter(date_time__range=[start, end])

        if request.GET.get('calculation') == "avg":
            sum, count = readings_sum(queryset)
            avg = sum / count
            return HttpResponse(avg)
        elif request.GET.get('calculation') == "sum":
            sum, count = readings_sum(queryset)
            return response.Response(sum)


def readings_sum(queryset):
    comulative_sum = 0
    number_of_readings = 0
    for obj in queryset:
        comulative_sum = comulative_sum + obj.Value
        number_of_readings = number_of_readings + 1
    return comulative_sum, number_of_readings

def func_pressure_readings(request, format=None):

     since = datetime.datetime.fromisoformat(request.GET.get('since'))
     until = datetime.datetime.fromisoformat(request.GET.get('until'))
     queryset = PressureReading.objects.filter(DateTime__range=[since, until])

     if request.GET.get('calculation') == "avg":
        sum, count = readings_sum(queryset)
        avg = sum/count
        return HttpResponse('Average= ' + str(avg))
     elif request.GET.get('calculation') == "sum":
        sum, count = readings_sum(queryset)
        return HttpResponse('Sum= ' +str(sum))
def check_if_missing_params(since, until, calculation):
    if since is None or until is None or calculation is None:
        return True


class Home(View):
    def get(self, request, *args ,**kwargs):
        return HttpResponse('Hello, World!')