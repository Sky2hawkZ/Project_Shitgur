# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 09:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_auto_20160530_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 11, 17, 32, 330000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 11, 17, 32, 329000)),
        ),
    ]