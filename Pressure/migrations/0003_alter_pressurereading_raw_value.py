# Generated by Django 4.0.6 on 2022-10-03 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pressure', '0002_pressurereading_raw_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressurereading',
            name='raw_value',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
