# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0010_auto_20180629_0006'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='trend',
            index=models.Index(fields=['-score', 'last_spotted_at', 'name'], name='trends_tren_score_87bf76_idx'),
        ),
    ]
