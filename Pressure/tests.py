from ast import And
from datetime import datetime
from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase

from .models import PressureReading, PressureSensor
import views

 # 1- check if The until argument has to be after the since argument. Otherwise it doesn’t make sense
class check_if_until_after_since(APITestCase):
    def check_if_until_after_since(self):
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2021-20-20')
     case_one = True if  since < until else False
     self.assertTrue(case_one == True, "since should be less than until.")

 # 2- check if It will only retrieve the readings that are within the time period specifie

class check_if_retrieve_since(APITestCase):
    def check_if_retrieve_since(self):
     pressure_sensor_obj = PressureSensor.objects.create(label='tubas_sensor', installation_date='2019-01-01', latitude='11.11',
                                           longitude='11.11')
     PressureReading.objects.create(sensor=pressure_sensor_obj, date_time='2020-02-02 02:02:02', value=2.2)
     PressureReading.objects.create(sensor=pressure_sensor_obj, date_time='2021-02-02 02:02:02', value=2.2)
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2021-20-20')
     result = PressureReading.objects.filter(date_time__range=[since, until])
     for item in result:
       self.assertTrue(since < item.date_time < until, "you have some objects not inside range")
  
 # 3- check if empty response
class check_if_empty_results(APITestCase):
    def check_if_empty_results(self):
     pressure_sensor_obj = PressureSensor.objects.create(label='tubas_sensor', installation_date='2019-01-01', latitude='11.11',
                                           longitude='11.11')
     PressureReading.objects.create(sensor=pressure_sensor_obj, date_time='2020-02-02 02:02:02', value=2.2)
     PressureReading.objects.create(sensor=pressure_sensor_obj, date_time='2021-02-02 02:02:02', value=2.2)
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2021-20-20')
     result = PressureReading.objects.filter(date_time__range=[since, until])
     self.assertNotEqual(result.count,0)

 # 4- check if sum correct
class check_if_sum_correct(APITestCase):
    def check_if_sum_correct(self):
     pressure_sensor_obj = PressureSensor.objects.create(label='tubas_sensor', installation_date='2019-01-01', latitude='11.11',
                                           longitude='11.11')
     PressureReading.objects.create(sensor=pressure_sensor_obj, date_time='2020-02-02 02:02:02', value=2.2)
     PressureReading.objects.create(sensor=pressure_sensor_obj, date_time='2021-02-02 02:02:02', value=2.2)
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2021-20-20')
     acumulative_sum = 0.0
     result = PressureReading.objects.filter(date_time__range=[since, until])
     for item in result:
        acumulative_sum = acumulative_sum + item.value
     self.assertEqual(acumulative_sum,4.4)

# 5- check if average correct
class check_if_avg_correct(APITestCase):
    def check_if_avg_correct(self):
     pressure_sensor_obj = PressureSensor.objects.create(label='tubas_sensor', installation_date='2019-01-01', latitude='11.11',
                                           longitude='11.11')
     PressureReading.objects.create(sensor=pressure_sensor_obj, date_time='2020-02-02 02:02:02', value=2.2)
     PressureReading.objects.create(sensor=pressure_sensor_obj, date_time='2021-02-02 02:02:02', value=2.2)
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2021-20-20')
     acumulative_sum = 0.0
     average = 0.0
     count = 0.0
     result = PressureReading.objects.filter(date_time__range=[since, until])
     for item in result:
        acumulative_sum = acumulative_sum + item.value
        count = count + 1 
     average = acumulative_sum/count
     self.assertEqual(average,2.2)
        
# 6- check if average correct

class check_if_missing_params(APITestCase):
    def check_if_missing_params(self):
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2021-20-20')
     self.assertFalse(views.check_if_missing_params(since, until, 'avg'))

# 7- check 404

class check_if_404(APITestCase):
    def check_if_404(self):
     since = datetime.datetime.fromisoformat('2010-10-10')
     until = datetime.datetime.fromisoformat('2021-20-20')
     result = PressureReading.objects.filter(date_time__range=[since, until])
     self.assertNotEqual(result.status_code , 405)