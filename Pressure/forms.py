

from Pressure.models import PressureReading, PressureSensor
from django import forms

class CreateSensorForm(forms.ModelForm):
    class Meta:
        model = PressureReading
        fields = ['ID', 'DateTime', 'Value' , 'SensorId']
        ID = forms.AutoField(primary_key=True)
        DateTime = forms.DateTimeField(auto_now_add=True)
        Value = forms.DecimalField(decimal_places=1, max_digits=3)
        SensorId = forms.ModelMultipleChoiceField (
            queryset=PressureSensor.objects.all(),
            widget=forms.CheckboxSelectMultiple
    )

    #   ID = models.AutoField(primary_key=True)
    # DateTime = models.DateTimeField(auto_now_add=True)
    # Value = models.DecimalField(decimal_places=1, max_digits=3)
    # # SensorId =  models.ForeignKey(PressureSensor,on_delete=models.CASCADE)
    # SensorId = models.ManyToManyField(PressureSensor)