from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import render, Http404
from django.db import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Post, Comment



def detail(request, post_id):
    try:
        p = Post.objects.get(pk=post_id)
        out = Comment.objects.filter(comment_post=post_id)
        p.post_views = getattr(p, 'post_views') +1;
        p.save()

    except p.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'post/detail.html', {'post': p, 'comment': out})






