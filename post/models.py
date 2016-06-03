from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.urlresolvers import reverse


class Post(models.Model):
    post_posted = models.DateTimeField(default=datetime.now())
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
    comment_posted = models.DateTimeField(default=datetime.now())
    comment_text = models.TextField(max_length=2000)
    comment_favorited = models.IntegerField(default=0)
    comment_points = models.IntegerField(default=0)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text

class Points_Post(models.Model):
    points_post_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    points_post_user = models.ForeignKey(User, on_delete=models.CASCADE)

    vote_post = {
        ('L', 'Like'),
        ('D', 'Dislike'),
        ('N', 'No vote'),
    }

    IsFavorited_post = {
        ('Y', 'Yes'),
        ('N', 'No'),
    }

    points_post_isFavorited = models.CharField(max_length=1, choices=IsFavorited_post, default='N', null=True)
    points_post_vote = models.CharField(max_length=1, choices=vote_post, default='N', null=True)

    def __str__(self):
        return  "Is favorited: " + self.points_post_isFavorited +" Voted: " + self.points_post_vote

class Points_Comment(models.Model):
    points_comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    points_comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    points_comment_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None)
    vote_comment = {
        ('L', 'Like'),
        ('D', 'Dislike'),
        ('N', 'No vote'),
    }

    IsFavorited_comment = {
        ('Y', 'Yes'),
        ('N', 'No'),
    }
    points_comment_isFavorited = models.CharField(max_length=1, choices=IsFavorited_comment, default='N', null=True)
    points_comment_vote = models.CharField(max_length=1, choices=vote_comment, default='N')

    def __str__(self):
        return "Is favorited: " + self.points_comment_isFavorited + " Voted: " + self.points_comment_vote



