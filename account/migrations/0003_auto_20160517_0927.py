# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160517_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='last_name',
        ),
    ]
