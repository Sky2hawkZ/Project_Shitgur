# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_post_favorited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(upload_to='files/images'),
        ),
    ]