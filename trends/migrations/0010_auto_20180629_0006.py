# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 07:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0009_auto_20180629_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='last_spotted_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
