
import time
from urllib import response


def Timing(get_response):

    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        duration = time.perf_counter() / 1000000
        print("the request " + request.path + " took " + f'{duration:.3f} ' +  " seconds to complete") 
        return response
    return middleware