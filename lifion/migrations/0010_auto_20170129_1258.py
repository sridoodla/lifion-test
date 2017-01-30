# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifion', '0009_questionresponse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='avg',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='score',
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='weighted_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]