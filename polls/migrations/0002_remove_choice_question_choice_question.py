# Generated by Django 4.0.6 on 2022-08-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ManyToManyField(to='polls.question'),
        ),
    ]
