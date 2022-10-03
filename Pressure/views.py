import datetime
from django.conf import settings
# from http.client import HTTPResponse
from django.http import HttpResponse
import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework import  viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response 
from rest_framework import viewsets, views
from rest_framework import response
from django.views import View
from Pressure.models import PressureReading, PressureSensor
from Pressure.serializer import PressureReadingSerializer, PressureSensorSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from rest_framework import permissions

# Create your views here.
import logging

from Pressure.utils import readings_sum
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
    #  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
     queryset = PressureSensor.objects.all()
     serializer_class = PressureSensorSerializer
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['ID', 'InstallationDate']



class PressureReadingViewSet(viewsets.ModelViewSet):
    #  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@login_required(login_url= settings.REDIRECT_URL)
def Home(request):
     user = authenticate(username='mohammad', password='Mhmad123@')
     if user is not None:
          # A backend authenticated the credentials
         return HttpResponse('Hi ' + user.username + "!")
     else:
        #  return HttpResponse('Hi Guest!')
           return redirect(settings.REDIRECT_URL)

# class Home(View):
#     def get(self, request, *args ,**kwargs):
#         user = authenticate(username='john', password='secret')
#         if user is not None:
#           # A backend authenticated the credentials
#          return HttpResponse('Hi Guest!')
#         else:
#          return HttpResponse('Hi Guest!')
#          No backend authenticated the credentials


# PURPUSE OF LOGGING : print out to consol or file , print logs of whats going on 

# logging types
#------ 1- DEBUG: when executed code or API requests include debugging parameters or headers

#------ 2- INFO:  the application entered a certain state
#---------- example :  INFO log level with information on which user requested authorization

#------ 3- WARNING:  the log level that indicates that something unexpected happened in the application but the code can continue the work.

#------ 4- ERROR: you can see time + errors -> these errors come from users activites and caused by somthing like not compatability in server configs
#--------- example: attachment image size is limited .

#------ 5- CRITICAL: crucial part of the application is not working and we are not delivering a business logic