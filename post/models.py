from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Post(models.Model):
    post_posted = models.DateTimeField('DateTime published')
    post_text = models.TextField(max_length=2000)
    post_points = models.IntegerField(default=0)
    post_views = models.IntegerField(default=0)
    post_favorited = models.IntegerField(default=0)
    post_image = models.ImageField()
    post_tags = models.CharField(max_length=1000, default=None)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_IsAdvertised = models.BooleanField(default='false')

    def __str__(self):
        return self.post_text


class Comment(models.Model):
    comment_posted = models.DateTimeField('DateTime published')
    comment_text = models.TextField(max_length=2000)
    comment_favorited = models.IntegerField(default=0)
    comment_points = models.IntegerField(default=0)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text




