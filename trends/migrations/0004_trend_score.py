# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0003_trend'),
    ]

    operations = [
        migrations.AddField(
            model_name='trend',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]
