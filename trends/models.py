# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)

class Trend(models.Model):
    name = models.CharField(max_length=32)
    score = models.IntegerField(default=1, null=False)
    