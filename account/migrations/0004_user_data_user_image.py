# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20160517_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='user_image',
            field=models.ImageField(default='static/account/user_images/default.jpg', height_field=800, upload_to='static/account/user_images', width_field=600),
        ),
    ]
