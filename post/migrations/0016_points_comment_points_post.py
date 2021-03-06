# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 05:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0015_auto_20160526_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_comment_isFavorited', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], default='N', max_length=1, null=True)),
                ('points_comment_vote', models.CharField(choices=[('D', 'Dislike'), ('L', 'Like')], default='N', max_length=1, null=True)),
                ('points_comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
                ('points_comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Points_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_post_isFavorited', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], default='N', max_length=1, null=True)),
                ('points_post_vote', models.CharField(choices=[('D', 'Dislike'), ('L', 'Like')], default='N', max_length=1, null=True)),
                ('points_post_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
                ('points_post_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
