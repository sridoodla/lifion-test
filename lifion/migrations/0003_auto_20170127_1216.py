# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifion', '0002_auto_20170127_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='lifionuser',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='lifion.Organization'),
        ),
    ]
