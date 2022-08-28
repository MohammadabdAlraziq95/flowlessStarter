from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import  viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from Pressure.models import PressureReading, PressureSensor
from Pressure.serializer import PressureReadingSerializer, PressureSensorSerializer
# Create your views here.






# class PressureSensorViewSet(viewsets.ViewSet):
#  queryset = PressureSensor.objects.all()
   
#  def list(self, request):
#   serializer_class = PressureSensorSerializer(self.queryset, many=True)
#   return Response(serializer_class.data)

# def retrieve(self, request, pk=None):
#     ps = get_object_or_404(self.queryset,pk=pk)
#     serializer_class = PressureSensorSerializer(ps)
#     return Response(serializer_class.data)
 
# def list(self, request):
#         pass

# def create(self, request):
#         pass

# def retrieve(self, request, pk=None):
#         pass

# def update(self, request, pk=None):
#         pass

# def partial_update(self, request, pk=None):
#         pass

# def destroy(self, request, pk=None):
#         pass

class PressureSensorViewSet(viewsets.ModelViewSet):

     queryset = PressureSensor.objects.all()
     serializer_class = PressureSensorSerializer
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['ID', 'InstallationDate']



class PressureReadingViewSet(viewsets.ModelViewSet):

     queryset = PressureReading.objects.all()
     # form_class = CreateSensorForm
     serializer_class = PressureReadingSerializer
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['ID', 'DateTime']
     