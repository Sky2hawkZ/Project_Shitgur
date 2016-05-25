from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# this file extends User and contains additional user data.

class user_data(models.Model):
    user = models.OneToOneField(User, unique=True)
    user_image = models.ImageField(upload_to='account/media/user_images',
                                   default='account/media/user_images/default.jpg')
    date_of_birth = models.DateField()
    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not specified'),
    }
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N', null=True)
    country = models.CharField(max_length=30)
    about = models.CharField(max_length=500)