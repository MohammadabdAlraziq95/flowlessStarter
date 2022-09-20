from django.http import HttpResponse

import logging
# we can see built in veriables here by printing logging
print (dir(logging))
logging.basicConfig(filename='polls.log', level='INFO', filemode="a" , format="time = %(asctime)s Logger_name = %(name)s level =  %(levelname)s message= %(message)s ")
log = logging.getLogger(__name__)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")