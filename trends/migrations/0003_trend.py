# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0002_keyword_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('first_spotted_at', models.TimeField()),
            ],
        ),
    ]
