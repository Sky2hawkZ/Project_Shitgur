from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms

# this file extends User and contains additional user data.

class user_data(models.Model):
    user = models.OneToOneField(User, unique=True)
    user_image = models.ImageField(upload_to='account/media/user_images', default='account/media/user_images/default.jpg', blank="True")
    date_of_birth = models.DateField(blank="True", null=True)
    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not specified'),
    }
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N')
    country = models.CharField(max_length=30, blank="True", null=True)
    about = models.TextField(blank="True", null=True)