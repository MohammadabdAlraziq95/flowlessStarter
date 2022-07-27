# Generated by Django 4.0.6 on 2022-07-27 10:18

import Pressure.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pressure', '0009_pressuresensor_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressuresensor',
            name='serial_number',
            field=models.CharField(default=Pressure.models.PressureSensor.compute_default, editable=False, max_length=100, null=True),
        ),
    ]
