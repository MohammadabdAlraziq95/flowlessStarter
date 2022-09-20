from ast import And
import datetime
import decimal
import imp
# from datetime import datetime
from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase
from django.utils import timezone
# from views import check_if_missing_params
import pytz
from Pressure.utils import readings_sum, check_if_missing_params

# import views

from .models import PressureReading, PressureSensor

 # 1- check if The until argument has to be after the since argument. Otherwise it doesn’t make sense
class PressureTestCase(TestCase):
 def test_if_until_after_since(self):
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2022-10-20')
     case_one = True if  since < until else False
     self.assertTrue(case_one == True, "since should be less than until.")
     PressureSensor.objects.create(Label='tubas_sensor', InstallationDate='2019-01-01', Latitude='11.11',
                                           Longitude='11.11')   
     PressureReading.objects.create( DateTime= datetime.datetime.now(tz=timezone.utc), Value=1 , raw_value = 2.2 )
     PressureReading.objects.create( DateTime= datetime.datetime.now(tz=timezone.utc), Value=1 , raw_value = 2.2 )
     result = PressureReading.objects.filter(DateTime__range=[since, until])
     for item in result:
      self.assertTrue(since < item.DateTime < until, "you have some objects not inside range")
  
#  3- check if empty response
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2012-10-20')
     PressureReading.objects.create( DateTime= datetime.datetime.now(tz=timezone.utc), Value=1 , raw_value = 2.2 )
     PressureReading.objects.create( DateTime= datetime.datetime.now(tz=timezone.utc), Value=1 , raw_value = 2.2 )
     result = PressureReading.objects.filter(DateTime__range=[since, until])
     self.assertNotEqual(result.count,0)

 # 4- check if sum correct
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2023-12-20')
     acumulative_sum = 0
     result = PressureReading.objects.filter(DateTime__range=[since, until])
     sum , count = readings_sum(result)
     self.assertEqual(float(sum),float(4))

# 5- check if average correct
     acumulative_sum = 0.0
     average = 0.0
     count = 0
     result = PressureReading.objects.filter(DateTime__range=[since, until])
     sum , count = readings_sum(result)
     average = sum/count
     self.assertEqual(average,1)
        
# # 6- check if average correct
     self.assertFalse(check_if_missing_params(since, until, 'avg'))

# # 7- check 404
    #  result = PressureReading.objects.filter(DateTime__range=[since, until])
    #  self.assertNotEqual(result.status_code , 405)
