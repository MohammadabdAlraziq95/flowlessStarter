# Generated by Django 4.0.6 on 2022-07-27 12:04

import Pressure.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pressure', '0011_alter_pressuresensor_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressuresensor',
            name='serial_number',
            field=models.CharField(default=Pressure.models.PressureSensor.compute_default, help_text=Pressure.models.PressureSensor.compute_default, max_length=100, null=True),
        ),
    ]