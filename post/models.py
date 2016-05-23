from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
    post_posted = models.DateTimeField('DateTime published')
    post_text = models.TextField(max_length=2000)
    post_likes = models.IntegerField(default=0)
    post_dislikes = models.IntegerField(default=0)
    post_image = models.FileField(upload_to='files/images')
    post_tags = models.CharField(max_length=1000, default=None)

    def __str__(self):
        return self.post_text


class GalleryPost(models.Model):
    GalleryPost_image = models.FileField(upload_to='files/images')
    GalleryPost_tags = models.CharField(max_length=250)
    GalleryPost_title = models.CharField(max_length=250)

def __str__(self):
    return self.GalleryPost_title
