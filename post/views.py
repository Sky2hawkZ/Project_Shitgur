from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import render, Http404, get_object_or_404
from django.db import models
from django.http import HttpResponse, Http404
from models import Post, Comment

def index(request):
    all_gallery_posts = Post.objects.all()
    context = {'all_gallery_posts': all_gallery_posts}
    return render(request, 'post/frontpage.html', context)

def detail(request, post_id):
    try:
        p = Post.objects.get(pk=post_id)
        c = Comment.objects.get(comment_post=p)
        p.post_views = getattr(p, 'post_views') +1;
        p.save()
    except p.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'post/detail.html', {'post': p, 'comment': c})
