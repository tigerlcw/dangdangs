# Generated by Django 2.2.3 on 2019-07-24 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20190724_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 24, 15, 9, 31, 202427)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 24, 15, 9, 31, 202427)),
        ),
    ]
