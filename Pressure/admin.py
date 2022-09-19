from django.contrib import admin

from Pressure.models import PressureReading, PressureSensor

# Register your models here.


@admin.register(PressureSensor)
class PressureSensorAdmin(admin.ModelAdmin):
    readonly_fields=('serial_number',)

admin.site.register(PressureReading)
