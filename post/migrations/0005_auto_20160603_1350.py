# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 20:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20160603_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 3, 13, 50, 55, 237000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 3, 13, 50, 55, 237000)),
        ),
    ]
