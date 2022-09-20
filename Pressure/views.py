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
import logging
# we can see built in veriables here by printing logging
print (dir(logging))

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from django.core import serializers

# config
logging.basicConfig(filename='my_app_log.log', level='INFO', filemode="a" , format="time = %(asctime)s Logger_name = %(name)s level =  %(levelname)s message= %(message)s ")
log = logging.getLogger(__name__)


apiCalledCounter = 0

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

        #  test info logging
        global apiCalledCounter
        apiCalledCounter = apiCalledCounter + 1
        log.info(apiCalledCounter)

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
        else: logging.error("this is critical issue")


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


# PURPUSE OF LOGGING : print out to consol or file , print logs of whats going on 

# logging types
#------ 1- DEBUG: when executed code or API requests include debugging parameters or headers

#------ 2- INFO:  the application entered a certain state
#---------- example :  INFO log level with information on which user requested authorization

#------ 3- WARNING:  the log level that indicates that something unexpected happened in the application but the code can continue the work.

#------ 4- ERROR: you can see time + errors -> these errors come from users activites and caused by somthing like not compatability in server configs
#--------- example: attachment image size is limited .

#------ 5- CRITICAL: crucial part of the application is not working and we are not delivering a business logic