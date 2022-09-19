
import datetime

def readings_sum(queryset):
    comulative_sum = 0
    number_of_readings = 0
    for obj in queryset:
        comulative_sum = comulative_sum + obj.Value
        number_of_readings = number_of_readings + 1
    return comulative_sum, number_of_readings


def check_if_missing_params(since, until, calculation):
     if since is None or until is None or calculation is None:
        return True